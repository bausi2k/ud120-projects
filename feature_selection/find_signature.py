#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file ="../text_learning/your_word_data.pkl"
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )


### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn.model_selection import train_test_split
#features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)
features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors, test_size=0.1, random_state=42) #updated for Library Version 0.2


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]

print("Training points: {}".format(len(features_train)))

### your code goes here
from sklearn import tree
from sklearn.metrics import accuracy_score


clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred_arr = clf.predict(features_test)


print("Score: {}".format(accuracy_score(labels_test, pred_arr)))
# The Code puts out 1.0, although the correct answer is: 0.948236632537
# https://discussions.udacity.com/t/lesson-12-accuracy-of-your-overfit-decision-tree-mini-lec-26/251831/17
# Dont have a clue why, the code ist correct compared to the suggestions in the forum...
print("Important features:")
checker = 0.0

for index, feature in enumerate(clf.feature_importances_):
    if feature > 0.02 and checker < feature:
        checker = feature
        print("Max feature at index {} with value {} ".format(index, feature))


from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer(stop_words='english')
#tfidf.fit_transform(word_data)
tfidf.fit_transform(word_data)
print(len(tfidf.get_feature_names()))

print(checker)
print(tfidf.get_feature_names()[33656])
print("Score after cleanup: {}".format(accuracy_score(labels_test, pred_arr)))   # print after feature clenaup