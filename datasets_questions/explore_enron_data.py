#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

j = 0

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
enron_names = open("../final_project/poi_names.txt", "r")
for person_name in enron_data:
    #print(person_name)
    if enron_data[person_name]["poi"] == 1:
        j = j + 1
        #print(enron_data[person_name]["poi"])

#print("Daten: ", j)


pois = 0
for names in enron_names:
    if names.find("("):
        print("no poi ")
    else:
        print(names)
        pois = pois + 1
print("Number of Pois: ", pois)

for person_name in enron_data:
    #print(person_name)
    if "prentice james" in person_name.lower():
        #print("Not James")
        #print(person_name)
        for key in enron_data[person_name]:
            if "stock" in key.lower():
                print(key, enron_data[person_name][key])