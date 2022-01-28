from decouple import config
import praw
#import pandas as pd


# Read-only Reddit instance
reddit = praw.Reddit(
    client_id = config('CLIENT_ID'), 
    client_secret= config('CLIENT_SECRET'),
    user_agent= config('USER_AGENT'))

#print(reddit.read_only)
# Output: True

# Obtain submission object
url = "https://www.reddit.com/r/AskReddit/comments/s9oaa6/what_is_the_most_beautiful_song_you_have_ever/"
submission = reddit.submission(url=url)

# Remove all "MoreComments" instances
submission.comments.replace_more(limit=0)

# Print out comments
for top_level_comment in submission.comments:
   print(top_level_comment.body)
     


    



