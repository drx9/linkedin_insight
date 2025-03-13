LinkedIn Insights Microservice
This project is a LinkedIn Insights Microservice that scrapes LinkedIn company pages to fetch details such as the company name, description, and follower count. The scraped data is stored in a MongoDB database, and RESTful APIs are provided to retrieve the data.

Features
Scraping: Scrapes LinkedIn company pages for details like name, description, and followers.

Database: Stores scraped data in MongoDB.

RESTful APIs: Provides endpoints to fetch company details from the database.

Filters: Allows filtering company pages by follower count and industry.

Pagination: Supports pagination for fetching multiple pages.

Challenges Faced:

Scraping Issues:
LinkedIn’s HTML Structure: LinkedIn frequently updates its HTML structure, making it difficult to maintain a stable scraper. The class names and tags used in the scraper often become outdated.

Login Requirements: LinkedIn requires login to access certain data, and the scraper may fail if login credentials are incorrect or if two-factor authentication (2FA) is enabled.

Blocking: LinkedIn may block automated scraping attempts, especially if too many requests are made in a short period.

Attempted Solutions
HTML Structure Updates: The scraper was updated multiple times to match LinkedIn’s changing HTML structure.

Login Automation: The scraper was modified to log in to LinkedIn using provided credentials.

Headless Mode: The scraper was run in headless mode to avoid detection.

Exclusion of LinkedIn API
The LinkedIn API was not used due to a lack of knowledge and the complexity of obtaining API access.

Setup Instructions
Follow these steps to set up and run the project locally.

1. Prerequisites
   
Python 3.9 or higher
MongoDB Atlas account (or local MongoDB instance)
ChromeDriver (matching your Chrome browser version)

Future Improvements:

Use LinkedIn API: If access to the LinkedIn API is obtained, it can provide a more reliable way to fetch company data.
Proxy Rotation: Use proxies to avoid being blocked by LinkedIn.
Error Handling: Improve error handling and retry mechanisms for the scraper.
AI Summaries: Use OpenAI’s ChatGPT API to generate summaries for company pages.

***Note: The scraping didn't work after trying different types of methods so i gave up because of the time limit***
