#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score
from pprint import pprint

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

## time tracking
t0 = time()
print(t0, "s")
print("start time:", round(time()-t0, 3), "s")

#pprint(features_train, indent=2)
print()
#pprint(labels_train, depth=4, indent=2)

clf.fit(features_train, labels_train)


t2 = round(time()-t0, 3)
print ("training time:", t2, "s")


labels_pred = clf.predict(features_test)
t3 = round(time()-t2-t0, 3)
print ("prediction time:", t3, "s")
print (labels_pred)

## accuracy
print (accuracy_score(labels_test, labels_pred))

#########################################################


