class Track:
    def __init__(self, name, id, artist, duration=0):
        self.name = name
        self.id = id
        self.artist = artist
        self.duration = duration
    
    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"

    def __str__(self):
        return f"{self.name} by {self.artist}"