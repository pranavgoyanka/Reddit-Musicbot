import praw
import prawcreds as pc
import codes_scopes as scopes

client_id = pc.client_id
client_secret = pc.client_secret
password = pc.password
user_agent = pc.user_agent
username = pc.username
redirect_uri = pc.redirect_uri

reddit = praw.Reddit(client_id = client_id,
					 client_secret = client_secret,
					 password = password,
					 user_agent = user_agent,
					 username = username, 
					 redirect_uri = redirect_uri)

# important scopes
# read - read content from posts
# submit - submit content, basically write posts and comments
# edit - edit posts and content
# all oauth scopes link - https://www.reddit.com/r/GoldTesting/comments/3chbrm/all_oauth_scopes/

scope = 'read'
message = ''

subreddit = reddit.subreddit('testingground4bots')

# obtain a permanent token

# url = reddit.auth.url([scope], '...', 'permanent')
# print(url)

# # assign code the rerturn url from the auth url
# # using already obtained code
# code = scopes.read
# print(code)
# print('\n')

# # Getting authorisation
# reddit.auth.authorize(code)

def botCallData(body):
	global message
	# format for data
	# !musicbot artist <artist_name> OR
	# !musicbot song <song_name> OR
	# !musicbot album <album_name> OR
	# !musicbot top5 <artist_name>
	# !musicbot bio <artist_name>
	info = body.split(' ')
	if info[0] == "!musicbot":
		if info[1] == 'artist':
			# spotify_api_call to be placed here
			print('artist is ' + info[1])
			message = 'artist is ' + info[2]

		elif info[1] == 'song':
			print('song')
			message = 'song is ' + info[2]
		elif info[1] == 'album':
			print('album')
			message = 'album is ' + info[2]
		elif info[1] == 'top5':
			print('top5')
			message = 'Here\'s a list of top 5 songs by' + info[2]
		elif info[1] == 'bio':
			print('bio')
			message = 'bio of ' + info[2]
		else:
			message = 'Invalid format'
	else:
		message = 'Am I not needed here?'



comments = subreddit.stream.comments()

for comment in comments:
	if '!musicbot' in comment.body.lower():
		botCallData(comment.body.lower())
		comment.reply(message)









