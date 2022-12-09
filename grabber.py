import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='86a607d1c9754bf4b133b0c7f005ae48', client_secret='f055259507c34fd08186fb1f06fdae2f'),)
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
 results = spotify.next(results)
 albums.extend(results['items'])
for album in albums:
 print(album['name'])
