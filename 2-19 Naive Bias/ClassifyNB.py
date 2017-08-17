def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    ### your code goes here!

 # from sklearn.naive_bayes import GaussianNB
 # clf = GaussianNB()
 # return clf.fit(features_train, labels_train)

    from sklearn.svm import SVC
    clf = SVC(kernel='poly', C=100.0, degree=4)
    return clf.fit(features_train, labels_train)