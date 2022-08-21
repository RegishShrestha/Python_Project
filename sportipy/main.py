
client__id="f811b3d4ee594bb090aef34351179b34"
client__screte="8f8f29c1e2664bcbafa45ccabd51ce4c"

import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

soup = BeautifulSoup(response.text, 'html.parser')

test = []
# song_list = []

# songs = soup.find_all("h3", class_="a-no-trucate")
song_names_spans = soup.find_all("h3", id="title-of-a-story", class_="a-no-trucate")
# for tag in songs:
#         test.append(tag.getText())

# for song in test:
#         song_list.append(song.replace("\n", ""))
songs= [song.getText().strip() for song in song_names_spans]
print(songs)
sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://localhost:8888/callback",
                client_id=client__id,
                client_secret=client__screte,
                cache_path="token.txt",
                show_dialog=True,
        )
)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in songs:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
# print(result)
        try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
        except IndexError:
                print(f"{song} doesn't exist /in Spotify. Skipped.")

playlists = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100." ,collaborative=False,public=False)

sp.playlist_add_items(playlist_id=playlists["id"], items=song_uris)
print(sp)