from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from app.database.db import pages_collection

COOKIES = {
    "li_at": "AQEDATu0mtIAwZ6gAAABlZAasS0AAAGVtCc1LVYAh6hvkvnjDAExGoQePnzUgOWfFq4GGNJ7KWg5Ck1SK2TCNlBbqeefS-IVic_HPdfGvikEEvXPRpmKpfnWc68b62cAv9jAqLrcfEio-ZLZ-l4nw_7w"
}

CHROMEDRIVER_PATH = "C:/chromedriver.exe"

def setup_driver():
    """Configures and launches Selenium WebDriver"""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")  

    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.linkedin.com")
    time.sleep(3)

    for name, value in COOKIES.items():
        driver.add_cookie({"name": name, "value": value})

    driver.refresh()
    time.sleep(3)

    return driver

def scrape_linkedin_page(linkedin_url):
    """Scrapes LinkedIn data for company pages, profiles, or job listings"""
    driver = setup_driver()

    driver.get(linkedin_url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
    except:
        print("Page failed to load.")
        driver.quit()
        return {"error": "Failed to load page"}
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    
    if "linkedin.com/company/" in linkedin_url:
        return extract_company_info(soup)
    elif "linkedin.com/in/" in linkedin_url:
        return extract_profile_info(soup)
    elif "linkedin.com/jobs/view/" in linkedin_url:
        return extract_job_info(soup)
    else:
        return {"error": "Unknown LinkedIn page type"}

def extract_company_info(soup):
    """Extracts company details from a LinkedIn page"""
    company_name = soup.find("h1")
    company_name = company_name.text.strip() if company_name else "N/A"

    description = soup.find("p", class_="org-about-us__description")
    description = description.text.strip() if description else "N/A"

    followers = soup.find("div", class_="org-top-card-summary__info-item")
    followers = followers.text.strip() if followers else "N/A"

    return {
        "type": "Company",
        "name": company_name,
        "description": description,
        "followers": followers,
    }

def extract_profile_info(soup):
    """Extracts user profile details from a LinkedIn profile"""
    profile_name = soup.find("h1")
    profile_name = profile_name.text.strip() if profile_name else "N/A"

    headline = soup.find("div", class_="text-body-medium break-words")
    headline = headline.text.strip() if headline else "N/A"

    location = soup.find("span", class_="text-body-small inline t-black--light break-words")
    location = location.text.strip() if location else "N/A"

    return {
        "type": "Profile",
        "name": profile_name,
        "headline": headline,
        "location": location,
    }

def extract_job_info(soup):
    """Extracts job details from a LinkedIn job listing"""
    job_title = soup.find("h1")
    job_title = job_title.text.strip() if job_title else "N/A"

    company = soup.find("a", class_="ember-view t-black t-normal")
    company = company.text.strip() if company else "N/A"

    location = soup.find("span", class_="topcard__flavor topcard__flavor--bullet")
    location = location.text.strip() if location else "N/A"

    return {
        "type": "Job",
        "title": job_title,
        "company": company,
        "location": location,
    }

def scrape_linkedin_page(page_id):


    scraped_data = {
        "page_id": page_id,
        "name": page_name,
        "description": description,
        "followers": followers,
    }

    result = pages_collection.insert_one(scraped_data)
    print(f"Inserted document with ID: {result.inserted_id}")

    return scraped_data

if __name__ == "__main__":
    urls = [
        "https://www.linkedin.com/company/microsoft/",  # Company Page
        "https://www.linkedin.com/in/satyanadella/",  # Profile Page
        "https://www.linkedin.com/jobs/view/1234567890/"  # Job Listing (Example ID)
    ]

    for url in urls:
        data = scrape_linkedin_page(url)
        print(data)
