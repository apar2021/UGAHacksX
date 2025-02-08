from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class AtlasClient():
    def __init__(self, atlas_uri, dbname):
        self.client = MongoClient(atlas_uri, server_api=ServerApi('1'))
        self.database = self.client[dbname]

    def ping(self):
        print("In ping")
        self.client.admin.command('ping')
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print("in except")
            print(e)

    def get_collection(self, collection_name):
        collection = self.database[collection_name]
        return collection
    
    def find(self, collection_name, filter = {}, limit=0):
        collection = self.get_collection(collection_name)
        items = list(collection.find(filter=filter, limit=limit))
        return items