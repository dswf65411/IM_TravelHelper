from pymongo import MongoClient
from mongoDB import Data as connectData
def connect():
    uri = "mongodb://localhost:27017"
    connData.client = MongoClient(uri)
    connData.db = connData.client['SA']
