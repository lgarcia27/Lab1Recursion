#CS2302 Data Structures
#Use of Recursion in order to determine and analyze whether a section of comments
#fit into  positive, negative, or normal category.
#Programmed by Luis Garcia.
#Last modified September 18, 2018.
#Instructor Diego Aguirre.
#RecursiveReddit

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw

reddit = praw.Reddit(client_id='vo3B1Fd51rupXg', #To obtain the ckient id I went into reddit and create an application.
                     client_secret='vrJEX_48mRmiouINsUfJUxAtRH4', # Client Secret was also created through reddit.
                     user_agent='lgarcia27' #This user agent is the one I created on reddit.
                     )


nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

# I created a group of lists which will be kept in an array.
normalList = [] # The Normal List will store the normal comments of reddit.
negativeList = [] # The Negative List will store the negative comments of reddit.
positiveList = [] # The Positive List will store the positive comments of reddit.

#My Code
# This method helps to test and classified whether a comment is negative or positive 
# with the use of a normal comment as a value.
def classificationComments(comment, x):
    neg = get_text_negative_proba(comment.body)
    pos = get_text_positive_proba(comment.body)
    if neg-x > pos-x:
        positiveList.append(comment.body) #Append will add items to the end of the list. 
    return negativeList.append(comment.body)
#This method will support if there is a reply to a comment or comments and determine
# if the comment will go as normal.
def determinationOfComments(comments, x):
    for oriComment in comments.list():
        if len(oriComment.subComments) < 1: 
            x = get_text_neutral_proba(oriComment.body)
            if x >= 0.50: # if 0.50 a comment will be classified as normal
                normalList.append(oriComment.body)
            return classificationComments(oriComment, x) 
            for reply in oriComment.subComments.list():
                determinationOfComments(reply.subComments)

#Code given
def get_text_negative_proba(text):
   return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
   return sid.polarity_scores(text)['neu'] # I used normal instead of neutral



def get_text_positive_proba(text):
   return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments




def main():
    comments = get_submission_comments('https://www.reddit.com/r/politics/comments/9glw1w/avenatti_on_possible_2020_presidential_run_im/')
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

    print(neg)

main()
