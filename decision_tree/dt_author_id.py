#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import numpy as np
from sklearn import tree
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

def submitAccuracies():
  return {"acc_min_samples_split":round(acc_min_samples_split_2,3)}

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
t0 = time()
print("start time:", round(time()-t0, 3), "s")

clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train, labels_train)

t2 = round(time()-t0, 3)
print ("training time:", t2, "s")

labels_pred = clf.predict(features_test)


t3 = round(time()-t2-t0, 3)
print ("prediction time:", t3, "s")

acc_min_samples_split_2 = accuracy_score(labels_test, labels_pred)


print(submitAccuracies())

#print(features_train.shape) # number of items and array headers
#print(len(features_train)) # -> Number of Items
#########################################################


