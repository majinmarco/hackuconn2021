import json

import requests

from track import Track
from playlist import Playlist

class SpotifyClient:

    def __init__(self, authorization_token, user_id):
        self.authorization_token = authorization_token
        self.user_id = user_id
        
    def get_last_played_track(self, limit=10):
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for track in response_json["items"]]
        return tracks

    def get_track_recommendations(self, seed_tracks, limit=50):
        seed_tracks_url = ""
        for seed_track in seed_tracks:
            seed_tracks_url += seed_track.id + ","
        seed_tracks_url = seed_tracks_url[:-1]
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for track in response_json["tracks"]]
        return tracks

    def create_playlist(self, name):
        data = json.dumps({
            "name":name,
            "description":"Recommedation tracks",
            "public": True
        })
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = self._place_post_api_request(url, data)
        response_json = response.json()

        playlist_id = response_json["id"]
        playlist = Playlist(name, playlist_id)
        return playlist

    def populate_playlist(self, playlist, tracks):
        tracks_uris = [tracks.create_spotify_uri() for track in tracks]
        data = json.dumps(tracks_uris)
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        response = self._place_post_api_request(url, data)
        response_json = response.json()
        return response_json

    def _place_post_api_request(self, url, data):
        response = requests.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.authorization_token}"
            }
        )

    def _place_get_api_resquest(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.authorization_token}"
            }
        )
        return response