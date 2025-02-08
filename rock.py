import os
from dotenv import load_dotenv
from atlas_client import AtlasClient
from band_member import BandMember
from band_team import BandTeam

load_dotenv()
ATLAS_URI = os.getenv('ATLAS_URI')
DB_NAME = 'rockserver'
# COLLECTION_NAME = 'embedded_movies'

client = AtlasClient(ATLAS_URI, DB_NAME)

client.ping()

member = BandMember("Test Username", "Pass123", "Test Name", ["Flute", "Drums"], ["Jamming"], [{"spotify":"link.com"}], [{"team_id":232}])
band = BandTeam("Band Name", ["Goal 1", "Goal 2"], ["Drums", "Triangle"], [{'member_id': 2910231, 'name': 'Sophie Green', 'role': 'Drums', 'instrument': 'Drums'},
{'member_id': 34567, 'name': 'Alex Carter', 'role': 'Bassist', 'instrument': 'Bass Guitar'}], 2)
client.setup()
cursor = client.find_members()
for m in cursor:
    print(m)

cursor = client.find_bands()
for b in cursor:
    print(b)
client.insert_member(member)
client.insert_band(band)
client.list_databases()


# --- TEST DATASET ---

# movies = client.find (collection_name=COLLECTION_NAME, limit=5)
# # movies = client.find(collection_name=COLLECTION_NAME, filter={"year": 1999}, limit = 5)
# print (f"Found {len (movies)} movies")

# # print out movie info
# for idx, movie in enumerate (movies):
#    print(f'{idx+1}\nid: {movie["_id"]}\ntitle: {movie["title"]},\nyear: {movie["year"]}\nplot: {movie["plot"]}\n')