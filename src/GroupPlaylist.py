"""
Author: Spencer Fleming
File Name: GroupPlaylist.py
Description: Interacts with client to retrieve artists and create a playlist
"""
import spotipy_tools.SpotipyAuth as auth

SPOTIFY_USERNAME = 'spotify-username' # replace with your spotify username
SPOTIFY_CLIENT_ID = 'spotify-client-id' # replace with your spotify client id
SPOTIFY_CLIENT_SECRET = 'spotify-client-secret' # replace with your spotify client secret id
SPOTIFY_REDIRECT_URI = 'spotify-redirect-uri' # replace with your spotify redirect uri

def main():
	spotify = auth.authorize_spotify_acct(SPOTIFY_USERNAME, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI)

if __name__ == '__main__':
    main()
