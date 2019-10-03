# Reddit-Article-Bot
Python bot that searches a subreddit's posts for a domain and replies to the post with the domain's content.

This bot can be used to post news articles in the coment section by simply adding the domain name and the HTML tags for the content desired, see *sample_bot.py* for how this bot can work. The *sample_bot.py* script checks the top posts in /r/ireland, checks for posts from rte.ie (a news website), and posts the article as a comment under the post (assuming a post from rte.ie is found).

### Required Installs 
bs4, requests, and praw will need to be installed to use this script, simply use pip like so:
```
pip install bs4
pip install requests
pip install praw
```
### Required File Setup
You will need to have a file named *praw.ini* in the same directory as *article_bot.py*


*praw.ini* should look like this:
```
[DEFAULT]
# A boolean to indicate whether or not to check for package updates.
check_for_updates=True

# Object to kind mappings
comment_kind=t1
message_kind=t4
redditor_kind=t2
submission_kind=t3
subreddit_kind=t5
trophy_kind=t6

# The URL prefix for OAuth-related requests.
oauth_url=https://oauth.reddit.com

# The URL prefix for regular requests.
reddit_url=https://www.reddit.com

# The URL prefix for short URLs.
short_url=https://redd.it

[bot_name_here]
client_id=
client_secret=
password=
username=
user_agent=
```
You will need to change the last five lines to the information obtained from the script you created at https://www.reddit.com/prefs/apps/ and your reddit account infromation. The user agent can be anything.


### Let me see an example!
First make sure you setup your *praw.ini* file as described above, then checkout *sample_bot.py*! 
*sampe_bot.py* shows how the bot could work for the /r/ireland subreddit and the domain rte.ie 
