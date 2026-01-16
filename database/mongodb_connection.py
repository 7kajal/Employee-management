from pymongo import MongoClient
import os
from dotenv import load_dotenv

def get_database():
    load_dotenv()
    client = MongoClient(os.getenv("MONGODB_URI"))
    return client["company_db"]
