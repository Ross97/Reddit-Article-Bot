# Reddit-Article-Bot
Python bot that searches a subs posts for a domain and replies to the post with the domain's content.

bs4, requests, and praw will need to be installed to use this script
```
pip install bs4
pip install requests
pip install praw
```

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


*sampe_bot.py* shows how the bot could work for the /r/ireland subreddit and the domain rte.ie 
