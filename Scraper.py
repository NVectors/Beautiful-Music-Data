from os import sep
from decouple import config
from matplotlib import artist
from numpy import extract
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
    if hasattr(comment, 'body') and hasattr(comment.author, 'name'):
        parse_comment(comment)

def parse_comment(comment):
    #Split comment body by line breaks into a list
    split_comment = comment.body.splitlines()

    for line in split_comment:
        #Ignore empty lines(' ') caused by splitlines()
        if len(line) == 0:
            break

        # Song title - Artist 
        if (' - ' in line) and not (' by ' in line):
            print(line,'\n', '-'*5)

            song_title = line[:line.index(' - ')]
            if ":" in song_title or "," in song_title:
                break
            print(song_title, '\n', '-'*20)

            artist = line[line.index('- ')+2:]
            if artist.endswith(('.')):
                artist = artist[:artist.index('.')]
                print(artist, '\n', '-'*20)
            else:
                print(artist, '\n', '-'*20)
                

        #print(line,'\n', '-'*5)
        #if  (' by ' in line) and not (',' in line):

        #    print(line,'\n', '-'*5)

            # song_title = line[:line.index(' by')]
            # if ":" in song_title or "," in song_title:
            #     break

            # print(song_title, '\n', '-'*20)

           

        #elif (' - ' in line):
        #    print(line, '\n', '-'*20) 

        #Need to figure out if ',' is used to seperate songs 
        #elif (' , ' in line): 


def main():
    # Obtain submission object
    url = "https://www.reddit.com/r/AskReddit/comments/s9oaa6/what_is_the_most_beautiful_song_you_have_ever/"
    get_comment(url)


if __name__ == '__main__':
    main()
    



