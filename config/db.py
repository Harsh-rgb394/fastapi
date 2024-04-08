from pymongo import MongoClient

uri = "mongodb+srv://harsh:77CGPM1vOMOhTl6i@cluster0.ns6blgf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client=MongoClient(uri)

db=client.studentdb

collection_name=db["students"]
