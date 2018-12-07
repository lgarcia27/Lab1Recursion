# CS2302 Data Structures
# Use of Recursion in order to determine and analyze whether a section of comments
# Fit into  positive, negative, or normal category.
# Programmed by Luis Garcia.
# Last modified September 18, 2018.
# Instructor Diego Aguirre.
# Lab1

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw

reddit = praw.Reddit(client_id='vo3B1Fd51rupXg', # To obtain the client id I went into reddit and create an application.
                     client_secret='vrJEX_48mRmiouINsUfJUxAtRH4', # Client Secret was also created through reddit.
                     user_agent='lgarcia27' # This user agent is the one I created on reddit.
                     )

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

# I created a group of lists which will be kept in an array.
normalList = [] # The Normal List will store the normal comments of reddit.
negativeList = [] # The Negative List will store the negative comments of reddit.
positiveList = [] # The Positive List will store the positive comments of reddit.

# My Code
# This method helps to test and classified whether a comment is negative or positive
# with the use of a normal comment as a value.
def classificationComments(comment, x):
    neg = get_text_negative_proba(comment.body)
    pos = get_text_positive_proba(comment.body)
    if neg-x > pos-x:
        positiveList.append(comment.body) #Append will add items to the end of the list.
    return negativeList.append(comment.body)


# This method will support if there is a reply to a comment or comments and determine
# if the comment will go as normal.
def process_comments(x):
    if len(x) == 0 or x is None:
        return [],[],[]

    positive, neutral, negative = [],[],[]

    # TESTING
    #print(x[0].body)
    #print()

    w = get_text_negative_proba(x[0].body)
    y = get_text_neutral_proba(x[0].body)
    z = get_text_positive_proba(x[0].body)

    prob = max(w,y,z)

    # IF the max is negative
    if prob == w:
        negative.append(x[0].body)
    # If the max is neutral
    elif prob == y:
        neutral.append(x[0].body)
    # If the max is positive
    else:
        positive.append(x[0].body)

    # Go to replies of current node
    # Temporarily store lists
    posT, neuT, negT = process_comments(x[0].replies)
    # Add reply elements to lists
    positive.extend(posT)
    neutral.extend(neuT)
    negative.extend(negT)

    # Process same-level comments
    posT, neuT, negT = process_comments(x[1:])
    # add reply element to lists
    positive.extend(posT)
    neutral.extend(neuT)
    negative.extend(negT)

    return positive, neutral, negative

# Code given
def get_text_negative_proba(text):
   return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
   return sid.polarity_scores(text)['neu']  # I used normal instead of neutral

def get_text_positive_proba(text):
   return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments


def main():
    comments = get_submission_comments('https://www.reddit.com/r/politics/comments/9glw1w/avenatti_on_possible_2020_presidential_run_im/')
    # comments2 = get_submission_comments()
    posList, neuList, negList = process_comments(comments)

    #Printing lists
    print("Positive list: ", posList, "\n")
    print("Neutral list: ", neuList, "\n")
    print("Negative list: ", negList, "\n")


    '''
    #line 73 provides a link which will acess the library of the comments and will help with testing purposes.
    #The reason I choose this URL is because I believe politics is a very controversial toppic where you can always find positive, neutral, and negative comments.
    # As far as testing purposes it is relevant.
    print(comments[0].body)
    print(comments[0].subComments[0].body)
   #print statements will help in maintaining the order of the comments rather than having all over the place.
   #print(positiveList)
   #// print('Positive Comments') # This print line will help into the organization of the code and will print "Positive 
   #Comments in order to follow easier were these specifics comments are.
   #print(negativeList)
   #//print('Negative Comments') # This print line will help into the organization of the code and will print "Negative 
   #Comments in order to follow easier were these specifics comments are.
   #print(normalList)
   #//print('Normal Comments') # This print line will help into the organization of the code and will print "Normal 
   #Comments in order to follow easier were these specifics comments are.

    neg = get_text_negative_proba(comments[0].subComments[0].body)

    print(neg)'''

main()
