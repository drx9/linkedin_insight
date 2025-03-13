from fastapi import APIRouter, HTTPException
from app.scraper.linkedin_scraper import scrape_linkedin_page
from app.database.db import pages_collection
from bson import ObjectId
from typing import Any, Dict

router = APIRouter()

def convert_objectid_to_str(data: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively convert ObjectId fields to strings."""
    for key, value in data.items():
        if isinstance(value, ObjectId):
            data[key] = str(value)
        elif isinstance(value, dict):
            data[key] = convert_objectid_to_str(value)
        elif isinstance(value, list):
            data[key] = [convert_objectid_to_str(item) if isinstance(item, dict) else item for item in value]
    return data

@router.get("/page/{page_id}")
async def get_page(page_id: str):
    # Check if the page exists in the database
    page = pages_collection.find_one({"page_id": page_id})
    if page:
        # Convert ObjectId fields to strings
        page = convert_objectid_to_str(page)
        return page

    # If not, scrape the page and store it in the database
    scraped_data = scrape_linkedin_page(page_id)
    result = pages_collection.insert_one(scraped_data)

    # Add the inserted ID to the response
    scraped_data["_id"] = str(result.inserted_id)
    return scraped_data