from pymongo import MongoClient
from mongoDB import Data
# from mongoDB import Data as connectData

def connect():
    if Data.db == 0:
        uri = "mongodb://hairy:okdavid@ds023373.mlab.com:23373/saproject"
        Data.client = MongoClient(uri)
        Data.db = Data.client['saproject']
    return Data.db

# def listConnect(region, school):
#
# def listConnect(region):
