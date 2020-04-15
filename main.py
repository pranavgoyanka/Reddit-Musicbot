import praw
import time
import logging
import traceback
from art import *
import os
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
runs = 0
reddit = praw.Reddit(client_id = client_id,
					 client_secret = client_secret,
					 password = password,
					 user_agent = user_agent,
					 username = username, 
					 redirect_uri = redirect_uri)

# Logging 
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename='./botlog.log', level=logging.WARNING, format='%(asctime)s  %(message)s',
                    datefmt='%m-%d %H:%M',)

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
	info = body.split(' ')
	if (info[0] == '/u/goodmusicbot' or info[0] == 'u/goodmusicbot'):
		spd.search(info[1], ' '.join(info[2:]))
		if spd.url==None:
			message	= "Sorry, I wasn't able to find that. Maybe include more keywords such as the artist and album names along with the track name. :[ " 
		message = 'Here you go: ' + (' '.join(info[2:])) + ' (%s)' %spd.url + ' :]'
		# print(info[2:])
		logging.warning(info[2:])
		return message
	else:
		message = "DONT REPLY"
		return message
		
def botify():
	for item in reddit.inbox.unread(limit=None):
		# print(repr(item))
		comment = item

		if(str(type(comment)) == "<class 'praw.models.reddit.comment.Comment'>"):
			try:
				# if(botCallData(comment.body)):
				botCallData(comment.body.lower())
				if(message!='DONT REPLY'):
					comment.reply(message + beepboop)
					# runs = runs + 1
				item.mark_read()
			except:
				print("Unexpected error:")
				logging.warning('Unexpected Error')
				traceback.print_exc()
				item.mark_read()
				time.sleep(10)
				# print(item)
				# print('Error!')

# Main Bot Call
width = os.get_terminal_size().columns
tprint('music bot', font='slant')
print('Made By Pranav Goyanka')

while(True):
	# print('run')
	# logging.warning('run')
	# readLogs(runs)
	botify()
	# storeLogs(runs)
	time.sleep(10)
