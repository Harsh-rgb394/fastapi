from pymongo import MongoClient
import os

uri =os.getenv("Mongo_url")
client=MongoClient(uri)

db=client.studentdb

collection_name=db["students"]
