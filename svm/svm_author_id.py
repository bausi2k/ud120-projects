#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy
from pprint import pprint


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

csetting = 10000
clf = SVC(kernel='rbf', C=csetting)
t0 = time()
print("start time:", round(time()-t0, 3), "s")

## reduce trainig data:
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

clf.fit(features_train, labels_train)

t2 = round(time()-t0, 3)
print ("training time:", t2, "s")

labels_pred = clf.predict(features_test)

t3 = round(time()-t2-t0, 3)
print ("prediction time:", t3, "s")
#print(t2, t3, t0, time())
print (labels_pred)

count = 0
counts = 0


numpy.savetxt("testerl.txt",labels_pred)
for i in labels_pred:
    if i == 1:
        # print("Chris ", i)
        count = count + 1
    elif i == 0:
        # print("Sara ", i)
        counts = counts + 1
    else:
        print("Rest ???", i)

print("Elemente in Pred: {:5,d}".format(len(labels_pred)))
print("Chris counts: {:5,d} mails, Sara: {:5,d}".format(count, counts))
## accuracy
print("Accuracy: {:1.3f} and C: {:9,d}".format(accuracy_score(labels_test, labels_pred), csetting))
#########################################################


