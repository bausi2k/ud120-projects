#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0
tempi = ""

for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        #if temp_counter < 200: #use this before Lesson 12
        if temp_counter > 0:
            path = os.path.join('..', path[:-1])
            #print(path)
            email = open(path, "r")
            emailcontent = email.read()
            ### use parseOutText to extract the text from the opened email
            tempi = parseOutText(email)


            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            tempi = tempi.replace("sara","")
            tempi = tempi.replace("shackleton","")
            tempi = tempi.replace("sachrisra","")
            tempi = tempi.replace("germani","")
            tempi = tempi.replace("shireman","")    #Added for Lesson 12-29
            tempi = tempi.replace("shiringhouectect","")    #Added for Lesson 12-29

            ### append the text to word_data
            word_data.append(tempi)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            #print(emailcontent)
            if emailcontent.find("X-From: Shackleton, Sara") != -1:
                from_data.append('0')
                #print("from sara")
            else:
                from_data.append('1')
                #print("not from sara!")

            email.close()

print("emails processed")
from_sara.close()
from_chris.close()

print("Word data 152: {}".format(word_data[152]))

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )


### in Part 4, do TfIdf vectorization here

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)
myvector = vectorizer.fit_transform(word_data)
myelements = vectorizer.get_feature_names()
#print(myelements)
print("Number of Features: {}".format(len(vectorizer.get_feature_names())))
#print(vectorizer.get_feature_names())
#print(myelements)
print("Element 34597: {}".format(myelements[34596]))
#The code should be correct, although the Quiz says no...
