from flask import Flask, render_template, request, jsonify,redirect, url_for
import os
from flask import session,flash
from models import RockMember,RockTeam
from atlas_client import AtlasClient
from pymongo import MongoClient
import json
from werkzeug.security import check_password_hash

# include client connection string here
app = Flask(__name__)
ATLAS_URI = os.getenv('ATLAS_URI')
DB_NAME = "rockserver"
client = AtlasClient(ATLAS_URI,DB_NAME)

@app.route("/")
@app.route("/index.html")
@app.route("/index")
def index():
    return render_template('index.html')
@app.route("/about")
@app.route("/about.html")
def about():
    return render_template('about.html')
@app.route("/artist-register.html",methods=['GET','POST'])
@app.route('/artist-register', methods=['GET','POST'])
def register_artist():
    if request.method == 'GET':
        # Render the artist registration page
        return render_template('artist-register.html')

    if request.method == 'POST':
        # Handle the form submission when the form is submitted
        profile_data = request.get_json()

        # Prepare the artist's data for insertion into MongoDB
        artist = {
            "username": profile_data.get("username"),
            "password": profile_data.get("password"),  # Ideally, hash the password before saving
            "name": profile_data.get("name"),
            "genre": profile_data.get("genre"),
            "gender": profile_data.get("gender"),
            "instrument": profile_data.get("instrument"),
            "collab_type": profile_data.get("collab_type"),
            "bio": profile_data.get("bio"),
            "teams": []  # This will be an empty list initially
        }

        # Create a RockMember instance (if this class exists in your code)
        rock_artist = RockMember(
            artist['username'],
            artist['password'],
            artist['name'],
            artist['gender'],
            artist['genre'],
            artist['instrument'],
            artist['collab_type'],
            artist['bio'],
            artist['teams']
        )

        # Insert the artist into MongoDB using your Atlas client
        result = client.insert_member(rock_artist)

        # Return a success message in JSON format
        response = {
            "status": "success",
            "message": "Profile Registered Successfully!",
        }
        return jsonify(response)
@app.route("/band-register",methods=['GET','POST'])
@app.route("/band-register.html",methods=['GET','POST'])
def band_register():
    if request.method == 'GET':
        return render_template('band-register.html')
    if request.method == 'POST':
        # Handle the form submission when the form is submitted
        profile_data = request.get_json()

        # Prepare the artist's data for insertion into MongoDB
        band = {
            "username": profile_data.get("username"),
            "password": profile_data.get("password"),  # Ideally, hash the password before saving
            "name": profile_data.get("band-name"),
            "goals": profile_data.get("goals"),
            "genres":profile_data.get("genres"),
            "instruments": profile_data.get("instruments"),
            "collab_types": profile_data.get("collab_types"),
            "bio": profile_data.get("bio"),
            "members": [],
            "member_count":0,
        }

        # Create a RockMember instance (if this class exists in your code)
        rock_band = RockTeam(
            band['username'],
            band['password'],
            band['name'],
            band['goals'],
            {"genres":band["genres"],"instruments":band["instruments"],"collaboration_types":band["collab_types"]},
            band['bio'],
            band['members'],
            band['member_count']
        )
        print(band)

        # Insert the artist into MongoDB using your Atlas client
        result = client.insert_band(rock_band)

        # Return a success message in JSON format
        response = {
            "status": "success",
            "message": "Profile Registered Successfully!",
        }
        return jsonify(response)
@app.route("/login.html", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        try:
            form_data = request.get_json()
            username = form_data['username']
            password = form_data['password']

            # Connect to MongoDB Atlas
            db_client = MongoClient(ATLAS_URI)
            db = db_client.rockserver

            # Check the rock_member collection first
            rock_member = db.rock_member.find_one({"username": username})

            if rock_member:
                # Compare the provided password with the stored password directly
                if rock_member['password'] == password:
                    return jsonify({'status': 'success', 'message': 'Login successful!', 'redirect_url': '/about'})
                else:
                    return jsonify({'status': 'error', 'message': 'Incorrect password.'})
            else:
                # Check the rock_team collection if user is not found in rock_member
                rock_team = db.rock_team.find_one({"username": username})

                if rock_team:
                    # Compare the provided password with the stored password directly
                    if rock_team['password'] == password:
                        return jsonify({'status': 'success', 'message': 'Login successful!', 'redirect_url': '/about'})
                    else:
                        return jsonify({'status': 'error', 'message': 'Incorrect password.'})
                else:
                    return jsonify({'status': 'error', 'message': 'Username not found.'})

        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
@app.route("/band-recs.html")
@app.route("/band-recs")
def band_recs():
    return render_template("band-recs.html")
@app.route("/artist-recs.html")
@app.route("/artist-recs")
def artist_recs():
    try:
        # Open and read the JSON file
        with open('test.json', 'r') as f:
            data = json.load(f)

        # Pass the JSON data to the template
        return render_template('artist-recs.html', data=data)

    except Exception as e:
        return f"Error reading JSON data: {e}"
if __name__ == "__main__":
    app.run(debug=True)