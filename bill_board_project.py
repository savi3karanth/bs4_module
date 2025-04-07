import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from pprint import pprint

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
USERNAME = os.environ.get('USERNAME')
REDIRECT_URI= os.environ.get('REDIRECT_URI')
SCOPE=os.environ.get('SCOPE')
ACCESS_TOKEN=os.environ.get('ACCESS_TOKEN')

url = "https://www.billboard.com/charts/hot-100/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(f'song_names: {song_names}')



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=SCOPE,
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,
    )
)
user_id = sp.current_user()["id"]
print(f"user_id: {user_id}\n")

sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)
auth_url = sp_oauth.get_authorize_url()
print("Please go to this URL and authorize:", auth_url)

redirected_url = input("Paste the URL you were redirected to here: ")
auth_url = sp_oauth.get_authorize_url()
print("Please go to this URL and authorize:", auth_url)


token_info = sp_oauth.get_access_token(redirected_url)
print(token_info)
sp = spotipy.Spotify(auth=token_info['access_token'])
print(sp)



date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# Initialize an empty list for song URIs
song_uris = []

# First, search for each song and populate song_uris
for song_name in song_names:
    result = sp.search(song_name, limit=1, type='track')
    if result['tracks']['items']:
        song_uris.append(result['tracks']['items'][0]['uri'])

# Now that song_uris is populated, create the playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# Print out the song URIs to verify they are correct
print(f"song_uris: {song_uris}\n")

# Now add the songs to the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print("Songs added to the playlist successfully!")