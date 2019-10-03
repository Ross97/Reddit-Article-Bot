# Simple Reddit article bot created by Ross Phelan, 03/10/2019
import praw, os, re, requests
from bs4 import BeautifulSoup


# Accepts the URL to search, element to find, attribute type, attribute value
# Example getArticle('https://www.DOMAIN_NAME.com/news/...', 'div', 'id', 'articleBody')
# Returns article text if successful
# Returns -1 if unsuccessful
def getArticle(url, element, attr_type, attr_value):
	try:
		response = requests.get(url)
	except ConnectionError:  
   		print('Error requesting', url)
   		return -1

	if response.status_code is not 200:
		print('Bad status code from ', url, response.status_code) 
		return -1

	# Find the article text using BeautifulSoup
	html = BeautifulSoup(response.text, "html.parser")
	if html.body.find(element, attrs={attr_type:attr_value}):
		return html.body.find(element, attrs={attr_type:attr_value}).text
	else:
		print('Cannot find', element, attr_type, attr_value, 'in', url)
		return -1



def main():

	YOUR_BOT_NAME_FROM_PRAW_INI = 'article_bot' # Must match bot name in praw.ini
	SUB_TO_SEARCH = 'ireland'
	DOMAIN_TO_FIND = 'rte.ie'
	ELEMENT = 'section'
	ATTR_TYPE = 'itemprop'
	ATTR_VALUE = 'articleBody'

	# Create a file or list to store posts already replied to
	# Prevents posting to the same post twice
	if not os.path.isfile('posts_replied_to.txt'):
	    posts_replied_to = []
	else:
	    with open('posts_replied_to.txt', 'r') as f:
	       posts_replied_to = f.read()
	       posts_replied_to = posts_replied_to.split('\n')
	       posts_replied_to = list(filter(None, posts_replied_to))

	# Account information (login info + keys) from praw.ini (stored in the same directory as this file)
	reddit = praw.Reddit(YOUR_BOT_NAME_FROM_PRAW_INI)
	
	# The subreddit to search
	subreddit = reddit.subreddit(SUB_TO_SEARCH)

	# Iterate over the top 100 posts in Hot
	for submission in subreddit.hot(limit=100):

		# Check the post has not already been replied to (id is unique for each post)
		if submission.id not in posts_replied_to: 

			# Check for the domain using re
			if re.search(DOMAIN_TO_FIND, submission.url, re.IGNORECASE):

				article = getArticle(submission.url, ELEMENT, ATTR_TYPE, ATTR_VALUE)
				if article is not -1:
					submission.reply(article)
					posts_replied_to.append(submission.id)
					print('Replied to: ' + submission.title)

	# Write back to posts_replied_to.txt
	with open('posts_replied_to.txt', 'w') as f:
	    for post_id in posts_replied_to:
	    	f.write(post_id + '\n')

main()