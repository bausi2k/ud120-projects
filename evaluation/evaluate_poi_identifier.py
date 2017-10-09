#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

F_train, F_test, L_train, L_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(F_train, L_train)

print(clf.score(F_test, L_test))

print("POIs predicted: {}".format(clf.predict(F_test))) #15-29
print("Test Labels: {}".format(L_test))                 #15-31
print("POIs in total: {}".format(len(F_test)))          #15-30

count = 0
truecounter = 0
for i in clf.predict(F_test):
    if i == 1 and L_test[count] == 1:
        truecounter += 1
    count += 1

print("How many predictions equals test_labels? {}".format(truecounter))    #15-31

print("Precision score: {}".format(precision_score(L_test, clf.predict(F_test))))
print("Recall score: {}".format(recall_score(L_test, clf.predict(F_test))))

