from decouple import config
import praw
import pandas as pd

# Read-only Reddit instance
reddit = praw.Reddit(
    client_id = config('CLIENT_ID'), 
    client_secret= config('CLIENT_SECRET'),
    user_agent= config('USER_AGENT'))

# Test
#print(reddit.read_only)
# Output: True

# Obtain submission object
url = "https://www.reddit.com/r/AskReddit/comments/s9oaa6/what_is_the_most_beautiful_song_you_have_ever/"
submission = reddit.submission(url=url)

# Reduce comments returned and sort comments by "top"
submission.comment_sort = 'top'
submission.comment_limit = 10000

# Remove all "MoreComments" instances
submission.comments.replace_more(limit=0)

# Comment id and comment body into a dataframe
comments = submission.comments
df_rows = [[ comment.id, comment.body] for comment in comments]
df = pd.DataFrame(df_rows, columns=['Comment ID','Body'])
df.to_csv('./data/comments_raw.csv')


    



