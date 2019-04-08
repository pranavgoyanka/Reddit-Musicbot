import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

#All spotify api requests called from here

username = 'theShadow800'
scope = 'user-library-read'
client_id='4722295458164ac09b1b0451a4831ca5'
client_secret='f175085e92e64c0cb9806385028082c0'
redirect_uri='https://google.com/'

token = 0
name = 'Radiohead'

# Get a new token
def getToken():
	token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
	print(token)
	return token

# Send a search query
def search(categ, name):
	global token
	if token:
		sp = spotipy.Spotify(auth=token) 
		results = sp.search(q=categ + name, type=categ)
		print(results)
	else:
		print('Acquiring Token...\n')
		token = getToken()
		search(categ, name)

#Read token saved in the file token.txt
def tokenFile():
	file =  open('token.txt', 'r')
	global token
	token = file.read()
	file.close()

# while(True):
# categ = input('Category: ')
# name = input('Name: ')

print(token)
# search(categ, name)

