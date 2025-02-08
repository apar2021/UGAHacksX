import os
from dotenv import load_dotenv
from atlas_client import AtlasClient
from band_member import BandMember
from band_team import BandTeam

load_dotenv()
ATLAS_URI = os.getenv('ATLAS_URI')
DB_NAME = 'sample_mflix'
COLLECTION_NAME = 'embedded_movies'

client = AtlasClient(ATLAS_URI, DB_NAME)
client.ping()

# --- TEST DATASET ---

# movies = client.find (collection_name=COLLECTION_NAME, limit=5)
movies = client.find(collection_name=COLLECTION_NAME, filter={"year": 1999}, limit = 5)
print (f"Found {len (movies)} movies")

# print out movie info
for idx, movie in enumerate (movies):
   print(f'{idx+1}\nid: {movie["_id"]}\ntitle: {movie["title"]},\nyear: {movie["year"]}\nplot: {movie["plot"]}\n')


