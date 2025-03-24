import json
import random
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from generate_data import DataGenerator
from openai_client import OpenAIClient
from typing import List, Dict, Any
import math


class AtlasClient():
    def __init__(self, atlas_uri, dbname=None):
        self.openai_client = OpenAIClient()
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

    def find_members(self, filter={}, limit=0):
        collection = self.database['rock_member']
        items = list(collection.find(filter=filter, limit=limit))
        return items

    def find_bands(self, filter={}, limit=0):
        collection = self.database['rock_band']
        items = list(collection.find(filter=filter, limit=limit))
        return items

    def calculate_match_score(self, band: Dict[str, Any], member: Dict[str, Any]) -> float:
        """Calculate a match score between a band and a member based on multiple factors."""
        score = 0.0
        weights = {
            'instruments': 0.4,
            'genres': 0.3,
            'collaboration_types': 0.3
        }

        # Calculate instrument match score
        instrument_matches = set(band['looking_for']['instruments']) & set(member['instruments'])
        instrument_score = len(instrument_matches) / max(len(band['looking_for']['instruments']), len(member['instruments']))
        score += instrument_score * weights['instruments']

        # Calculate genre match score
        genre_matches = set(band['looking_for']['genres']) & set(member['genre'])
        genre_score = len(genre_matches) / max(len(band['looking_for']['genres']), len(member['genre']))
        score += genre_score * weights['genres']

        # Calculate collaboration type match score
        collab_matches = set(band['looking_for']['collaboration_types']) & set(member['collaboration_type'])
        collab_score = len(collab_matches) / max(len(band['looking_for']['collaboration_types']), len(member['collaboration_type']))
        score += collab_score * weights['collaboration_types']

        return score

    def recommend_members(self, band_id: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Recommend members for a band based on multiple matching criteria."""
        band_search = self.find_bands(filter={"_id": ObjectId(band_id)})
        if not band_search:
            print('No band found!')
            return []

        band = band_search[0]
        print("Band Info:", band)

        # Get all potential members
        potential_members = self.find_members()
        
        # Calculate match scores for each member
        scored_members = []
        for member in potential_members:
            match_score = self.calculate_match_score(band, member)
            scored_members.append({
                'member': member,
                'score': match_score
            })

        # Sort by match score and get top matches
        scored_members.sort(key=lambda x: x['score'], reverse=True)
        top_matches = scored_members[:limit]

        # Print recommendations
        print("\nRecommended Members:")
        for match in top_matches:
            member = match['member']
            score = match['score']
            print(f"{member['name']} | Score: {score:.2f}")
            print(f"Instruments: {member['instruments']}")
            print(f"Genre: {member['genre']}")
            print(f"Collaboration Type: {member['collaboration_type']}")
            print("---")

        # Get AI recommendations
        self.openai_client.artist_recommendation(band, [m['member'] for m in top_matches])
        
        return top_matches

    def recommend_band(self, member_id: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Recommend bands for a member based on multiple matching criteria."""
        member_search = self.find_members(filter={"_id": ObjectId(member_id)})
        if not member_search:
            print('No member found!')
            return []

        member = member_search[0]
        print("Member Info:", member)

        # Get all potential bands
        potential_bands = self.find_bands()
        
        # Calculate match scores for each band
        scored_bands = []
        for band in potential_bands:
            match_score = self.calculate_match_score(band, member)
            scored_bands.append({
                'band': band,
                'score': match_score
            })

        # Sort by match score and get top matches
        scored_bands.sort(key=lambda x: x['score'], reverse=True)
        top_matches = scored_bands[:limit]

        # Print recommendations
        print("\nRecommended Bands:")
        for match in top_matches:
            band = match['band']
            score = match['score']
            print(f"{band['name']} | Score: {score:.2f}")
            print(f"Looking for: {band['looking_for']}")
            print(f"Goals: {band['goals']}")
            print("---")

        # Get AI recommendations
        self.openai_client.band_recommendation(member, [b['band'] for b in top_matches])
        
        return top_matches

    def insert_member(self, band_member):
        self.database.rock_member.insert_one(band_member.__dict__)

    def insert_band(self, band_team):
        self.database.rock_band.insert_one(band_team.__dict__)