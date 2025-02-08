import json
import random
import os
from dotenv import load_dotenv
from models import RockMember, RockTeam

load_dotenv()
generated_members = int(os.getenv('GENERATE_MEMBERS'))
generated_bands = int(os.getenv('GENERATE_BANDS'))
band_instruments = ["Drums", "Flute", "Triangle", "Bass Guitar", "Vocals", "Violin", "Cello"]
genres = ["Punk", "Heavy Metal", "Classic Rock", "Indie", "Grunge"]
collab_types = ["Jamming", "Song Writing", "Band Colab", "Rock Battle"]

with open("generation/first_names.json", 'r') as f:
     first_names = json.loads(f.read())
     
with open("generation/last_names.json", 'r') as f:
     last_names = json.loads(f.read())

with open("generation/adjectives.json", 'r') as f:
     adjectives = json.loads(f.read())

with open("generation/nouns.json", 'r') as f:
     nouns = json.loads(f.read())

with open("generation/goals.json", 'r') as f:
     band_goals = json.loads(f.read())

print(len(first_names))
print(len(last_names))

band_members = []
bands = []
for i in range(generated_members):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    username = f"{first_name}{last_name}{i}"
    password = f"{100000+i}"
    name = f"{first_name} {last_name}"
    genre = random.sample(genres, random.choice([1, 1, 1, 2]))
    instruments = random.sample(band_instruments, random.choice([1, 1, 1, 1, 2, 2, 3]))
    collab = random.sample(collab_types, random.choice([1, 1, 1, 1, 2]))
#     social_link = f"{first_name}{last_name}.com"
    teams = []
    
    member = RockMember(username, password, name, genre, instruments, collab, teams)
    band_members.append(member.__dict__)


for i in range(generated_bands):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    band_name = f"{adj} {noun}"
    goals = random.sample(band_goals, 2)
    looking_for_instrument = random.sample(band_instruments, random.choice([1, 1, 1, 1, 2]))
    looking_for_genre = random.sample(genres, random.choice([1, 1, 1, 1, 2]))
    looking_for_collab = random.sample(collab_types, random.choice([1, 1, 1, 1, 2]))
    looking_for = {'instruments': looking_for_instrument, 'genres': looking_for_genre, 'collaboration_types': looking_for_collab}
    members = []
    member_count = 0

    band = RockTeam(band_name, goals, looking_for, members, member_count)
    bands.append(band.__dict__)

with open("generation/band_members.json", "w") as f:
     f.write(json.dumps(band_members))

with open("generation/bands.json", "w") as f:
     f.write(json.dumps(bands))


print("done")