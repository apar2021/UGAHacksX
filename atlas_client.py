import os
import json
import random
from openai import OpenAI
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from generate_data import DataGenerator

class AtlasClient():
    def __init__(self, atlas_uri, dbname=None):
        load_dotenv()
        api_key = os.getenv('OPENAI_KEY')
        self.openai_client = OpenAI(api_key=api_key)
        self.client = MongoClient(atlas_uri, server_api=ServerApi('1'))
        if dbname:
            self.database = self.client[dbname]
    
    def setup(self):
        if 'rockserver' not in self.client.list_database_names():
            rock_db = self.client["rockserver"]
            rock_db.create_collection("rock_member")
            rock_db.create_collection("rock_band")
            self.generator = DataGenerator()
            self.insert_test_data()
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
    
    def recommend_members(self, band_id):
        band_search = self.find_bands(filter = {"_id": ObjectId(band_id)})
        if band_search:
            band = band_search[0]
            print("Band Info")
            print(band)
            looking_for_instrument = band['looking_for']['instruments']
            looking_for_genre = band['looking_for']['genres']
            looking_for_collab = band['looking_for']['collaboration_types']
            print()
            print(looking_for_instrument)
            print(looking_for_collab)
            print(looking_for_genre)

            print("")
            print("Recommended Members")
            member_search = self.find_members(
                filter = {"$and": [{'instruments': {'$in': looking_for_instrument}}, 
                         {'genre': {'$in': looking_for_genre}},
                         {'collaboration_type': {'$in': looking_for_collab}}
                         ]})
            if not member_search:
                print("No available artists!")
                return
            if len(member_search) > 3:
                member_search = random.sample(member_search, 3)
            for m in member_search:
                print(f"{m['name']} | {m['instruments']}, {m['genre']}, {m['collaboration_type']}")
            self.openai_artist_recommendation(band, member_search)
        else:
            print('No band found!')

    def recommend_band(self, member_id):
        member_search = self.find_members(filter = {"_id": ObjectId(member_id)})
        if member_search:
            member = member_search[0]
            print("Member Info")
            print(member)
            instruments = member['instruments']
            genres = member['genre']
            collab = member['collaboration_type']
            print()
            print(instruments)
            print(collab)
            print(genres)
            print("")
            print("Recommended Bands")
            band_search = self.find_bands(
                filter = {"$and": [{'looking_for.instruments': {'$in': instruments}}, 
                         {'looking_for.genres': {'$in': genres}},
                         {'looking_for.collaboration_types': {'$in': collab}}
                         ]})
            if not band_search:
                print("No available bands!")
                return
            if len(band_search) > 3:
                band_search = random.sample(band_search, 3)
            for b in band_search:
                print(f"{b['name']} | {b['looking_for']['instruments']}, {b['looking_for']['genres']}, {b['looking_for']['collaboration_types']}")
            self.openai_band_recommendation(member, band_search)
        else:
            print('No member found!')

    def openai_band_recommendation(self, member, bands):
        bands_str = "\n".join([f"{i+1}. Band Name is {bands[i]['name']}. {bands[i]['bio']}" for i in range(len(bands))])
        output_format = '{"band_number": band_number, "explanation": explanation}'
        print("OPENAI QUERY")
        content = f"""Here is my bio as a rock band member. {member['bio']}

Here are bios for {len(bands)} rock bands
{bands_str}

Which band would be the best fit for me? Print out the band number with a short explanation of 2-3 sentences. The output should be in the format {output_format}"""
        completion = self.openai_client.chat.completions.create(
            messages=[{
            "role": "user",
            "content": content,
            }],
            model="gpt-4o")
        print("OPENAI QUERY")
        print(content)
        print("OPENAI RESULT")
        print(completion.choices[0].message.content)

    def openai_artist_recommendation(self, band, members):
        members_str = "\n".join([f"{i+1}. Artist Name is {members[i]['name']}. {members[i]['bio']}" for i in range(len(members))])
        output_format = '{"artist_number": aritst_number, "explanation": explanation}'
        print("OPENAI QUERY")
        content = f"""Here is my bio as a rock band. {band['bio']}

Here are bios for {len(members)} rock artists
{members_str}

Which artist would be the best fit for my band? Print out the artist number with a short explanation of 2-3 sentences. The output should be in the format {output_format}"""
        completion = self.openai_client.chat.completions.create(
            messages=[{
            "role": "user",
            "content": content,
            }],
            model="gpt-4o")
        print("OPENAI QUERY")
        print(content)
        print("OPENAI RESULT")
        print(completion.choices[0].message.content)

    def insert_member(self, band_member):
        self.database.rock_member.insert_one(band_member.__dict__)

    def insert_band(self, band_team):
        self.database.rock_band.insert_one(band_team.__dict__)
