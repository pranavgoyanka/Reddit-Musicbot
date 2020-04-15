import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import creds
import string
#All spotify api requests called from here

username = creds.username
scope = creds.scope
client_id= creds.client_id
client_secret= creds.client_secret
redirect_uri= creds.redirect_uri
url = ''
# wrongurl = ''
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

	if categ == 'track':
		cat = 'tracks'
	if categ == 'artist':
		cat = 'artists'
	if categ == 'album':
		cat = 'albums'

	if len(results[cat]['items']) == 0:
		url = None
	data(categ)
	improvedDataRanked(categ, name)

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


# Improved search
# fields to check
# results['tracks']['items'][0]['artists'][0]['name']
# results['tracks']['items'][0]['name']
# results['tracks']['items'][0]['album']['name']


# Keep Checking Approach (incomplete rn)
def improvedData(categ, q):
	global url
	query = q.split()
	if categ == 'track':
		for res in results['tracks']['items']:
			keepChecking = 1
			for n in res['name']:
				if n in query:
					query.remove(n)
				else:
					keepChecking = 0
			if keepChecking:
				for n in res['artists'][0]['name']:
					if n in query:
						query.remove(n)
					else:
						keepChecking = 0
			if keepChecking:
				for n in res['album']['name']:
					if n in query:
						query.remove(n)

def improvedDataRanked(categ, q):
	global url
	# global wrongurl
	checkString = []
	minScore = 3.1
	maxScore = 0
	if categ == 'track':
		cat = 'tracks'
	if categ == 'artist':
		cat = 'artists'
	if categ == 'album':
		cat = 'albums'

	for res in results[cat]['items']:
		query = q.translate(str.maketrans('', '', string.punctuation)).split()
		checkString = []
		lenQ = len(query)
		score = 0
		try: checkString = checkString + res['name'].split()
		except: pass
		try: checkString = checkString + res['artists'][0]['name'].split()
		except: pass
		try: checkString = checkString + res['album']['name'].split()
		except: pass
		
		checkString = ' '.join(str(c) for c in checkString)
		checkString = checkString.translate(str.maketrans('', '', string.punctuation))
		checkString = checkString.split()


		lenC = len(checkString)
		# print('-----------------ITEM---------------')
		# print(checkString)
		# print(lenC)
		# print(query)
		if len(checkString) != 0:
			for el in checkString:
				if el.lower() in query:
					# print(el.lower())
					checkString.remove(el)
					query.remove(el.lower())

			score = (2*len(checkString)/lenC) + (len(query)/lenQ)
			
			# print(checkString)
			# print(query)
			# print(score)

			# Wrong Algorithm
			# if score > maxScore:
			# 	maxScore = score
			# 	wrongurl = res['external_urls']['spotify']
			
			# Minimise Score for better accuracy
			if score < minScore:
				minScore = score
				url = res['external_urls']['spotify']


# while(True):
# categ = input('Category: ')
# name = input('Name: ')

# print(token)
# search(categ, name)

