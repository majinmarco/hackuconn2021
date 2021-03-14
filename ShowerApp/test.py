import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = '1230853848'

token = SpotifyOAuth(client_id="e219391ab9f741e6b4f6d1a54a5910a4", client_secret="3afc7a77d5f344418295213b88abf87c", redirect_uri="http://127.0.0.1:8080/",scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

#create the playlist
playlist_name = input("Enter a playlist name ")
playlist_description = input("Enter the playlist description: ")

spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description="Songs to shower to!")

user_input = input("Enter the song: ")
list_of_songs = []

while user_input != 'quit':
    result = spotifyObject.search(q=user_input)
    #print(json.dumps(result, sort_keys=4, indent=4))
    #print(result['tracks']['items'][0]['uri'])
    list_of_songs.append(result['tracks']['items'][0]['uri'])
    user_input = input('Enter another song or enter "quit"')

prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=list_of_songs)