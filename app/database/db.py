from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.linkedin_insights

pages_collection = db.pages
posts_collection = db.posts
comments_collection = db.comments