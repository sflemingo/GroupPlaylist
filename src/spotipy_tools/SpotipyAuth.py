"""
Author: Spencer Fleming
File Name: SpotipyAuth.py
Description: Authorizes the Spotify account with spotipy
"""
import spotipy
import spotipy.util as util

def authorize_spotify_acct(username, client_id, client_secret, redirect_uri):
	"""
	authorizes the spotify account
	returns the spotify object
	"""
	scope = 'playlist-modify-public'
	token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
	if token:
		spotify = spotipy.Spotify(auth=token)
		return spotify		
	else:
		sys.exit("Can't retrieve token")
