import spotipy
import spotipy.oauth2 as oauth2

credentials = oauth2.SpotifyClientCredentials(
        client_id='bc0780e21dee47309a4789d08e52e0da',
        client_secret='707c58cee7c24455b7ec4496ba2d9bd8')

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)

name = 'Ed Sheeran'

results = spotify.search(name)

#Extract Ed Sheeran's artist uri (ID)
artist_uri = results['tracks']['items'][0]['artists'][0]['uri']

#Pull up all of Ed Sheeran's albums
edsheeran_albums = spotify.artist_albums(artist_uri, album_type = 'album')

album_names = []
album_uris = []
for i in range(len(edsheeran_albums['items'])):
	album_names.append(edsheeran_albums['items'][i]['name'])
	album_uris.append(edsheeran_albums['items'][i]['uri'])

print "album names: ", album_names, "\n"
print "album uris: ",album_uris


def albumSongs(uri):
	album = uri
	