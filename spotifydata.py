import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import creds

#All spotify api requests called from here

username = creds.username
scope = creds.scope
client_id= creds.client_id
client_secret= creds.client_secret
redirect_uri= creds.redirect_uri
url = ''
token = 0
name = 'Radiohead'
results = ''
# def redditRequest(type, name):



# Get a new token
def getToken():
	token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
	# print(token)
	return token

# Send a search query
# def search(categ, name):
# 	global token
# 	global results
# 	if token:
# 		token = getToken()
# 		sp = spotipy.Spotify(auth=token) 
# 		results = sp.search(q=categ + ':'+ name, type=categ)
# 		print(results)
# 		return results
# 	else:
# 		print('Acquiring Token...\n')
# 		token = getToken()
# 		search(categ, name)

def search(categ, name):
	global token
	global results
	token = getToken()
	sp = spotipy.Spotify(auth=token) 
	results = sp.search(q=name, type=categ)
	data(categ)

#Read token saved in the file token.txt
def tokenFile():
	file =  open('token.txt', 'r')
	global token
	token = file.read()
	file.close()

def data(categ):
	global url
	if categ == 'track':
		url = results['tracks']['items'][0]['external_urls']['spotify']

	elif categ == 'artist':
		url = results['artists']['items'][0]['external_urls']['spotify']

	elif categ == 'album':
		url = results['albums']['items'][0]['external_urls']['spotify']


# while(True):
# categ = input('Category: ')
# name = input('Name: ')

# print(token)
# search(categ, name)

