"""
Author: Spencer Fleming
File Name: SpotipySearch.py
Description: Handles searches for artists with spotipy
"""
import spotipy

def search_single_artist(spotify, artist_name):
	"""
	performs a spotify search on an artist
	returns the artist's uri
	"""
	results = spotify.search(q='artist:' + artist_name, type='artist')
	uri = results['artists']['items'][0]['uri']
	return uri

def artist_top_ten(spotify, artist_uri):
	"""
	returns the artist's top ten track uris
	"""
	ret = set()
	top_tracks = spotify.artist_top_tracks(artist_uri)
	tracks = top_tracks['tracks']
	for i in range(10):
		if(len(tracks) <= i): break
		ret.add(tracks[i]['uri'])
	return ret

