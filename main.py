from fastapi import FastAPI
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from pathlib import Path
from Routes.studentRoute import router


# for env file securing 
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app=FastAPI()
# without reload it wont work like nodemon like run again again /





app.include_router(router)







