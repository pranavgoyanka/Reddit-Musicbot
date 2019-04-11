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

for submissions in reddit.subreddit('testingground4bots').top(limit = 35):
	print(submissions.title)


