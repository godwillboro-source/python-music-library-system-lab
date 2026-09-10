class Song:
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    def add_song_to_count(self):
        if not hasattr(Song, 'count'):
            Song.count = 0
        Song.count += 1

    def add_to_genres(self):
        if not hasattr(Song, 'genres'):
            Song.genres = []
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if not hasattr(Song, 'artists'):
            Song.artists = []
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        if not hasattr(Song, 'genre_count'):
            Song.genre_count = {}
        Song.genre_count[self.genre] = Song.genre_count.get(self.genre, 0) + 1

    def add_to_artists_count(self):
        if not hasattr(Song, 'artist_count'):
            Song.artist_count = {}
        Song.artist_count[self.artist] = Song.artist_count.get(self.artist, 0) + 1


