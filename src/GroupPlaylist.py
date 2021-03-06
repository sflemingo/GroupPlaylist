"""
Author: Spencer Fleming
File Name: GroupPlaylist.py
Description: Interacts with client to retrieve artists and create a playlist
"""
import spotipy_tools.SpotipyAuth as auth
import spotipy_tools.SpotipySearch as search
import spotipy_tools.SpotipyPlaylist as playlist
import random

SPOTIFY_USERNAME = 'spotify-username' # replace with your spotify username
SPOTIFY_CLIENT_ID = 'spotify-client-id' # replace with your spotify client id
SPOTIFY_CLIENT_SECRET = 'spotify-client-secret' # replace with your spotify client secret id
SPOTIFY_REDIRECT_URI = 'spotify-redirect-uri' # replace with your spotify redirect uri

def prompt_artist_names():
	"""
	prompts the reader to input artist names
	returns set of artist names
	"""
	ret = set()
	line = input('Enter artist names:\n')
	while(len(line) > 0):
		ret.add(line)
		if(len(ret) >= 10) : break
		line = input()
	return ret

def main():
	spotify = auth.authorize_spotify_acct(SPOTIFY_USERNAME, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI)
	playlist_name = input('Enter new playlist name: ')
	artist_names = prompt_artist_names()
	track_uris = set()
	for artist_name in artist_names:
		artist_uri = search.search_single_artist(spotify, artist_name)
		artist_tracks = search.artist_top_ten(spotify, artist_uri)
		if (len(artist_tracks) > 5):
			artist_tracks = random.sample(artist_tracks, 5)
		track_uris = track_uris|set(artist_tracks)
	playlist_uri = playlist.create_playlist(spotify, SPOTIFY_USERNAME, playlist_name)
	playlist.add_tracks_to_playlist(spotify, SPOTIFY_USERNAME, playlist_uri, track_uris)

if __name__ == '__main__':
    main()
