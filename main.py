from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

SPOTIPY_CLIENT_ID="YOUR_SPOTIPY_CLIENT_ID"
SPOTIPY_CLIENT_SECRET="YOUR_SPOTIFY_CLIENT_SECRET"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

html_doc = requests.get(f"https://www.billboard.com/charts/hot-100/{date}").text
soup = BeautifulSoup(html_doc, 'html.parser')

songs = soup.find_all("span", class_="chart-element__information__song")
song_names = [i.getText() for i in songs]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")











#TODO: 1. Scrape the Billboard Hot 100 for the songs of a particular date.✅
#TODO: 2. Authenticate with Spotify. ✅
#TODO: 3. Search Spotify with the scraped songs from Todo 1.✅
#TODO: 4. Create and add a spotify playlist.
