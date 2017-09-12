#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import numpy as np

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
max = (0,0)
max = np.amax(data, axis=0)
print("Max element: ", max[0], max[1])

for i in data_dict:
    if data_dict[i]["salary"] == max[0]:
        print("Biggest Bonus winner: {}".format(i))
        print("These are the values of the Bonus Winner: ", data_dict[i])

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
#matplotlib.pyplot.show()
