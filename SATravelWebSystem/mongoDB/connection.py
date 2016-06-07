from pymongo import MongoClient
# from mongoDB import Data as connectData

def connect():
    uri = "mongodb://hairy:okdavid@ds023373.mlab.com:23373/saproject"
    client = MongoClient(uri)
    db = client['saproject']
    return db

# def listConnect(region, school):
#
# def listConnect(region):
