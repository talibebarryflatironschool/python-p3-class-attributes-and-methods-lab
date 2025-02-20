# class Song:
#     pass



class Song:
    # Class attributes to track songs, unique artists, unique genres, and histograms.
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes for an individual song.
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level tracking attributes
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        # Increment the count of songs.
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add genre to the genres list if it is not already present.
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Add artist to the artists list if not already present.
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Increment the count for the given genre.
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # Increment the count for the given artist.
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage:
song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("God's Plan", "Drake", "Rap")
song3 = Song("Halo", "Beyonce", "Pop")

print(Song.count)         # => 3
print(Song.artists)       # => ['Jay-Z', 'Drake', 'Beyonce']
print(Song.genres)        # => ['Rap', 'Pop']
print(Song.genre_count)   # => {'Rap': 2, 'Pop': 1}
print(Song.artist_count)  # => {'Jay-Z': 1, 'Drake': 1, 'Beyonce': 1}
