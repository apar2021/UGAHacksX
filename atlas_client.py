import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class AtlasClient():
    def __init__(self, atlas_uri, dbname=None):
        self.client = MongoClient(atlas_uri, server_api=ServerApi('1'))
        if dbname:
            self.database = self.client[dbname]
    
    def setup(self):
        if 'rockserver' not in self.client.list_database_names():
            rock_db = self.client["rockserver"]
            rock_db.create_collection("rock_member")
            rock_db.create_collection("rock_band")
        else:
            print('Rockserver Database already exists!')

    def insert_test_data(self):
        with open("generation/band_members.json", 'r') as f:
            self.database.rock_member.insert_many(json.loads(f.read()))
        with open("generation/bands.json", 'r') as f:
            self.database.rock_band.insert_many(json.loads(f.read()))

    def list_databases(self):
        print(self.client.list_database_names())

    def ping(self):
        self.client.admin.command('ping')
        try:
            self.client.admin.command('ping')
            print("Connected to MongoDB successfully!")
        except Exception as e:
            print("Oh no the connection to MongoDB failed :(")
            print(e)
    
    def find_members(self, filter = {}, limit=0):
        collection = self.database['rock_member']
        items = list(collection.find(filter=filter, limit=limit))
        return items
    
    def find_bands(self, filter = {}, limit=0):
        collection = self.database['rock_band']
        items = list(collection.find(filter=filter, limit=limit))
        return items    
    
    def insert_member(self, band_member):
        self.database.rock_member.insert_one(band_member.__dict__)

    def insert_band(self, band_team):
        self.database.rock_band.insert_one(band_team.__dict__)
