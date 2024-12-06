import os
from bs4 import BeautifulSoup
import requests
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()
client_id = os.environ["SPOTIFY_CLIENT_ID"]
client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]

# Spotify redirect URI (used during authentication)
spotify_redirect_uri = "http://example.com"

# Spotify OAuth setup with required permissions for playlist modification
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=spotify_redirect_uri,
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
    )
)

# Get the current user's Spotify ID
user_id = sp.current_user()["id"]

# Prompt user for the date of the Billboard Hot 100 chart
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]  # Extract the year for Spotify search queries

# Define headers for the web scraping request
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# Fetch the Billboard Hot 100 webpage for the specified date
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}", headers=header)
billboard_webpage = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(billboard_webpage, "html.parser")

# Select song names from the parsed HTML
songs_name_tag = soup.select("li ul li h3")
songs_list = [song_name.get_text().strip() for song_name in songs_name_tag]  # List of top 100 songs

# Initialize a list to hold Spotify URIs of the songs
song_uris = []

# Search for each song on Spotify
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")  # Search query includes track name and year
    try:
        # Get the URI of the first search result
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        # Handle case where no results are found
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create a new private playlist on Spotify
my_new_playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    description=f"Top Tracks from back in {date}"
)

# Add the collected song URIs to the newly created playlist
sp.playlist_add_items(playlist_id=my_new_playlist["id"], items=song_uris)

# Confirmation message
print(f"Playlist '{date} Billboard 100' created successfully!")
