import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
from mergesort import merge_sort
import json

scope = 'playlist-modify-public'
username = '1230853848'

token = SpotifyOAuth(client_id="e219391ab9f741e6b4f6d1a54a5910a4", client_secret="3afc7a77d5f344418295213b88abf87c", redirect_uri="http://127.0.0.1:8080/",scope='user-read-recently-played', username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

recently_listened = spotifyObject.current_user_recently_played()

recently_listened_uri_list = [track["track"]["uri"] for track in recently_listened["items"]]

recently_listened_uri_list_sliced = []
for x in range(5):
    recently_listened_uri_list_sliced.append(recently_listened_uri_list[random.randint(0, len(recently_listened_uri_list)-1)])

recommended_songs= spotifyObject.recommendations(seed_tracks=recently_listened_uri_list_sliced, limit=50)["tracks"]

recommended_songs_uri = []
for i in range(len(recommended_songs)):
    recommended_songs_uri.append(recommended_songs[i]["uri"])

recommended_songs_audio_features = spotifyObject.audio_features(tracks=recommended_songs_uri)

recommended_songs_bpm = sorted(recommended_songs_audio_features, key = lambda i: i['energy'])    

def sum_time(l, time):
    for i in range(len(l)):
        time+=(l[i]["duration_ms"]/1000)

    return time * 60

sum_of_time = sum_time(recommended_songs, 0)

while 11>sum_of_time>10:
    x = random.randint(0, len(recommended_songs_bpm))
    sum_of_time -= recommended_songs_bpm[x]["duration_ms"]/1000
    del recommended_songs_bpm[x]

final_track_list = [recommended_songs_bpm[track]["uri"] for track in range(len(recommended_songs_bpm))]

prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=final_track_list)