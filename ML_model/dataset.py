from pydoc import cli
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os, csv
from dotenv import load_dotenv
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

        
generate_data()


