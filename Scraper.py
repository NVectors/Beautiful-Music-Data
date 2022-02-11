from decouple import config
import praw
import pandas as pd

# Read-only Reddit instance
reddit = praw.Reddit(
    client_id = config('CLIENT_ID'), 
    client_secret= config('CLIENT_SECRET'),
    user_agent= config('USER_AGENT'))

def get_comment(url):
    submission = reddit.submission(url=url)
    submission.comment_sort = 'top'
    submission.comment_limit = 10000
    submission.comments.replace_more(limit=0)
    
    for comment in submission.comments:
        read_comment(comment)

def read_comment(comment):
    if hasattr(comment, 'body'):
        print(comment.body)

def main():
    # Obtain submission object
    url = "https://www.reddit.com/r/AskReddit/comments/s9oaa6/what_is_the_most_beautiful_song_you_have_ever/"
    get_comment(url)


if __name__ == '__main__':
    main()
    



