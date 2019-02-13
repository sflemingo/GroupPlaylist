"""
Author: Spencer Fleming
File Name: SpotipyPlaylist.py
Description: Handles spotipy playlist creation
"""
import spotipy

def create_playlist(spotify, playlist_name):
	"""
	creates a new playlist on the user's account
	returns the playlist's uri
	"""
	playlist = spotify.user_playlist_create(username, 'sptest')

def add_tracks_to_playlist(spotify, playlist_uri, track_uris):
	"""
	add tracks to the playlist
	"""
