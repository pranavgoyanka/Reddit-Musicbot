import praw
# from praw.model import Message
import prawcreds as pc
import codes_scopes as scopes
import spotifydata as spd
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
name = ''

beepboop = '''\n\nBeep Boop, I am a bot\n
			Please upvote me so that I can work more often'''

def botCallData(body):
	global message
	# format for data
	# !musicbot artist <artist_name> OR
	# !musicbot track <song_name> OR
	# !musicbot album <album_name> OR
	# !musicbot top5 <artist_name>
	# !musicbot bio <artist_name>
	info = body.split(' ')
	# if info[0] == "!musicbot":
	# 	if info[1] == 'artist':
	# 		# spotify_api_call to be placed here
	# 		print('artist is ' + info[1])
	# 	elif info[1] == 'song':
	# 		print('song')
	# 		message = 'song is ' + info[2]
	# 	elif info[1] == 'album':
	# 		print('album')
	# 		message = 'album is ' + info[2]
	# 	elif info[1] == 'top5':
	# 		print('top5')
	# 		message = 'Here\'s a list of top 5 songs by' + info[2]
	# 	elif info[1] == 'bio':
	# 		print('bio')
	# 		message = 'bio of ' + info[2]
	# 	else:
	# 		message = 'Invalid format'
	# else:
	# 	message = 'Am I not needed here?'

	if (info[0] == '/u/goodmusicbot' or info[0] == 'u/goodmusicbot'):
		spd.search(info[1], ' '.join(info[2:]))
		message = 'Here you go: ' + (' '.join(info[2:])) + ' (%s)' %spd.url
		print(info[2:])
		return message
	else:
		return 'Am I needed here?'

# comments = subreddit.stream.comments()
# fn6ia2c
# for comment in comments:
# 	if '!musicbot' in comment.body.lower():
# 		try:
# 			botCallData(comment.body.lower())
# 			comment.reply(message + beepboop)
# 		except:
# 			print('Error!')

# Message read

def botify():
	for item in reddit.inbox.unread(limit=None):
		# print(repr(item))
		comment = item

		if(str(type(comment)) == "<class 'praw.models.reddit.comment.Comment'>"):
			try:
				# if(botCallData(comment.body)):
				botCallData(comment.body.lower())
				comment.reply(message + beepboop)
				item.mark_read()
			except:
				print("Unexpected error:")
				# print(item)
				# print('Error!')

while(True):
	botify()


# Mention Read
# for mention in reddit.inbox.mentions(limit=None):
#     print('{}\n{}\n'.format(mention.author, mention.body))