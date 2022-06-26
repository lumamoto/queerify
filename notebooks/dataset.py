import spotipy
import spotipy.util as util
from spotipy import SpotifyException
from spotipy.oauth2 import SpotifyClientCredentials
import os
import csv
from dotenv import load_dotenv
import re

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

redirect_uri = 'http://localhost:8888/callback'
scope = 'user-top-read playlist-modify-public'


def get_user_token():
    token = util.prompt_for_user_token(
        scope=scope,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=redirect_uri
    )
    spotify = spotipy.Spotify(auth=token)
    return spotify


def save_data(output_file='data/data.csv'):
    spotify = get_user_token()

    try:
        tracks = spotify.current_user_top_tracks(limit=50, time_range='long_term')['items']
    except SpotifyException as err:
        print(f'Exception Occurred: {err}')

    with open(output_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['artist_name', 'track_uri', 'artist_uri', 'track_name',
                         'album_uri', 'duration', 'album_name', 'artists'])
        for track in tracks:
            # URI
            track_uri = track['uri']

            # Track name
            track_name = track['name']

            # Main Artist
            artist_uri = track['artists'][0]['uri']
            # artist_info = spotify.artist(artist_uri)

            #Name, popularity, genre
            artist_name = track['artists'][0]['name']
            # artist_pop = artist_info['popularity']
            # artist_genres = artist_info['genres']

            # Album
            album_name = track['album']['name']
            album_uri = track['album']['uri']
            duration = track['duration_ms']
            artists = ', '.join([artist['name']
                                for artist in track['artists']])

            # Popularity of the track
            # track_pop = track['popularity']
            writer.writerow([artist_name, track_uri, artist_uri, track_name,
                             album_uri, duration, album_name, artists])


def ari_to_features(ari):
    client_credentials_manager = SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Audio features
    features = sp.audio_features(ari)[0]

    # Artist of the track, for genres and popularity
    artist = sp.track(ari)['artists'][0]['id']
    artist_pop = sp.artist(artist)['popularity']
    artist_genres = sp.artist(artist)['genres']

    # Track popularity
    track_pop = sp.track(ari)['popularity']

    # Add in extra features
    features['artist_pop'] = artist_pop
    if artist_genres:
        features['genres'] = ' '.join(
            [re.sub(' ', '_', i) for i in artist_genres])
    else:
        features['genres'] = 'unknown'
    features['track_pop'] = track_pop

    return features


save_data(output_file='data/user_top_tracks.csv')
