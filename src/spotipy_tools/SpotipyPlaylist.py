"""
Author: Spencer Fleming
File Name: SpotipyPlaylist.py
Description: Handles spotipy playlist creation
"""
import spotipy

def create_playlist(spotify, username, playlist_name):
	"""
	creates a new playlist on the user's account
	returns the playlist's uri
	"""
	playlist = spotify.user_playlist_create(username, playlist_name)
	return playlist['uri']

def add_tracks_to_playlist(spotify, username, playlist_uri, track_uris):
	"""
	add tracks to the playlist
	"""
	spotify.user_playlist_add_tracks(username, playlist_uri, track_uris)
