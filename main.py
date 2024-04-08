from fastapi import FastAPI
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
from Routes.studentRoute import router
app=FastAPI()
# without reload it wont work like nodemon like run again again /





app.include_router(router)







