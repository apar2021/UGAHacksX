import streamlit as st
from PIL import Image

def display_profile(user_profile):
    st.markdown("""
        <style>
            .profile-container {
                background-color: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            .profile-title {
                text-align: center;
                font-size: 28px;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<div class='profile-container'><h2 class='profile-title'>{user_profile['name']}'s Profile</h2></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/150", width=150)
    with col2:
        st.subheader("Basic Information")
        st.write(f"**Instrument:** {user_profile['instrument']}")
        st.write(f"**Experience Level:** {user_profile['experience_level']}")
        st.write(f"**Location:** {user_profile['location']}")
    
    st.markdown("---")
    
    st.subheader("Collaboration Preferences")
    st.write(f"**Types:** {', '.join(user_profile['collaboration_type'])}")
    st.write(f"**Availability:** {', '.join(user_profile['availability'])}")
    
    st.markdown("---")
    
    st.subheader("Social Links")
    col1, col2 = st.columns(2)
    with col1:
        for platform, link in user_profile['social_links'].items():
            st.markdown(f"<a style='font-size:18px;' href='{link}' target='_blank'>{platform.capitalize()}</a>", unsafe_allow_html=True)
    
# Sample User Profile
def main():
    st.sidebar.header("Band Participation")
    participation_choice = st.sidebar.radio("Would you like to:", ["Start a Band", "Join a Band"], index=0)
    
    if participation_choice == "Start a Band":
        role = "Hire Musicians"
    else:
        role = "Join a Band"
    
    st.sidebar.header("Enter Your Profile Details")
    name = st.sidebar.text_input("Name", "Sophie Green")
    instrument = st.sidebar.text_input("Instrument", "Drums")
    experience_level = st.sidebar.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"], index=1)
    location = st.sidebar.text_input("Location", "Austin, Texas")
    collaboration_type = st.sidebar.multiselect("Collaboration Type", ["Jamming", "Songwriting", "Recording", "Performing"], ["Jamming", "Songwriting"])
    availability = st.sidebar.multiselect("Availability", ["Mornings", "Afternoons", "Evenings", "Weekends"], ["Evenings", "Weekends"])
    spotify = st.sidebar.text_input("Spotify Profile URL", "https://spotify.com/user/sophiegreen")
    instagram = st.sidebar.text_input("Instagram Profile URL", "https://instagram.com/sophiegreenmusic")
    
    user_profile = {
        'name': name,
        'instrument': instrument,
        'experience_level': experience_level,
        'location': location,
        'collaboration_type': collaboration_type,
        'availability': availability,
        'social_links': {
            'spotify': spotify,
            'instagram': instagram
        },
        'role': role
    }
    
    st.sidebar.markdown(f"### Selected Role: **{role}**")
    display_profile(user_profile)

if __name__ == "__main__":
    main()
