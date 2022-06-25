from pydoc import cli
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os, csv
from dotenv import load_dotenv
import glob
import pandas as pd
import re
load_dotenv()
cid=os.getenv('cid')
client_secret=os.getenv('client_secret')



def save_data(link=None,output_file='data/data.csv'):
    client_credentials_manager=SpotifyClientCredentials(client_id=cid,
    client_secret=client_secret)
    session=spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    playlist_link = "https://open.spotify.com/playlist/7pA5BPAz7gRKQ8RAAMjbf7?si=f58d4607a9ea47c3"
    if link!=None:
        playlist_link=link
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    tracks=session.playlist_tracks(playlist_URI)['items']
    with open(output_file,'w',encoding='utf-8') as file:
        writer=csv.writer(file)
        writer.writerow(['artist_name','track_uri','artist_uri','track_name',\
        'album_uri','duration','album_name','artists'])
        for track in tracks:
            #URI
            track_uri = track["track"]["uri"]
    
            #Track name
            track_name = track["track"]["name"]
    
            #Main Artist
            artist_uri = track["track"]["artists"][0]["uri"]
            artist_info = session.artist(artist_uri)
    
            #Name, popularity, genre
            artist_name = track["track"]["artists"][0]["name"]
            # artist_pop = artist_info["popularity"]
            # artist_genres = artist_info["genres"]
    
            #Album
            album_name = track["track"]["album"]["name"]
            album_uri=track['track']['album']['uri']
            duration=track["track"]["duration_ms"]
            artists = ", ".join(
            [artist["name"] for artist in track["track"]["artists"]])
            #Popularity of the track
            # track_pop = track["track"]["popularity"]
            writer.writerow([artist_name,track_uri,artist_uri,track_name,\
            album_uri,duration,album_name,artists])

        
def generate_dataset():
    save_data(link='https://open.spotify.com/playlist/37i9dQZF1DWYdV3Fs5eWjC?si=f9f6c669575b433e'\
    ,output_file='data/data1.csv')
    save_data(link='https://open.spotify.com/playlist/09LRzqN5YKbiMZrJ29tB4r?si=73669677a61847db'\
    ,output_file='data/data2.csv')
    save_data(link='https://open.spotify.com/playlist/5GIrdzOEabFNOtFwSISifM?si=69e6c9ed02884498'\
    ,output_file='data/data3.csv')
    save_data(output_file='data/data4.csv')
    save_data(link='https://open.spotify.com/playlist/4MSg3vB23KtBZEF6Bx5TzS?si=48548b89aa194f3b'\
    ,output_file='data/data5.csv')
    save_data(link='https://open.spotify.com/playlist/0HuloRIml4hNBlJhCVWe1T?si=bd89f940d2b14d3f'\
    ,output_file='data/data6.csv')
    save_data(link='https://open.spotify.com/playlist/35MZThasjOKls4Cyy7RsoQ?si=35667e0f1e32462e'\
    ,output_file='data/data7.csv')

    files=os.path.join('data/','data*.csv')
    joined_list=glob.glob(files)
    df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
    df.to_csv('data/dataset.csv')

# generate_dataset()

def ari_to_features(ari):


    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    #Audio features
    features = sp.audio_features(ari)[0]
    
    #Artist of the track, for genres and popularity
    artist = sp.track(ari)["artists"][0]["id"]
    artist_pop = sp.artist(artist)["popularity"]
    artist_genres = sp.artist(artist)["genres"]
    
    #Track popularity
    track_pop = sp.track(ari)["popularity"]
    
    #Add in extra features
    features["artist_pop"] = artist_pop
    if artist_genres:
        features["genres"] = " ".join([re.sub(' ','_',i) for i in artist_genres])
    else:
        features["genres"] = "unknown"
    features["track_pop"] = track_pop
    
    return features
