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
import pprint
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
print("Number of Pois:  ", pois)

#prentice james 6-18
for person_name in enron_data:
    #print(person_name)
    if "prentice james" in person_name.lower():
        #print("Not James")
        #print(person_name)
        for key in enron_data[person_name]:
            if "stock" in key.lower():
                print(key, enron_data[person_name][key])
print("#### END Lesson 6-18")


#Wesley Colwell 6-19
for person_name in enron_data:
     #print(person_name)
     if "wesley" in person_name.lower():
         #print("Not James")
         pprint.pprint(enron_data[person_name])
         for key in enron_data[person_name]:
             if "from_this_person_to_poi" in key.lower():
              print(key, enron_data[person_name][key])
print("#### END Lesson 6-19")




#Jeffrey K Skilling 6-20
for person_name in enron_data:
     #print(person_name)
     if "skilling" in person_name.lower():
         print("Person: {}".format(person_name))
         pprint.pprint(enron_data[person_name])
         for key in enron_data[person_name]:
             if "stock" in key.lower():
              print(key, enron_data[person_name][key])
print("#### END Lesson 6-20")

#total_payments 6-25
for person_name in enron_data:
    #print(person_name)
    if "skilling" in person_name.lower():
        print("Person: {}".format(person_name))
        print("Total Payment: {}".format(enron_data[person_name]["total_payments"]))
    elif "lay" in person_name.lower():
        print("Person: {}".format(person_name))
        print("Total Payment: {}".format(enron_data[person_name]["total_payments"]))
    elif "fastow" in person_name.lower():
        print("Person: {}".format(person_name))
        print("Total Payment: {}".format(enron_data[person_name]["total_payments"]))
print("#### END Lesson 6-25")

#No. email and salary values 6-27
salc = 0
emailc = 0
for person_name in enron_data:
    #print(person_name)
    if enron_data[person_name]["salary"] != "NaN":
        salc = salc + 1
        #print("Name: {} with salary: {}".format(person_name,enron_data[person_name]["salary"]))
    if enron_data[person_name]["email_address"] != "NaN":
        #print("Name: {} with email: {}".format(person_name, enron_data[person_name]["email_address"]))
        emailc = emailc + 1

print("Valid salaries : {}; valid emails: {}".format(salc, emailc))
print("#### END Lesson 6-27")

#total_payments 6-29
tpayc = 0
count = 0
for person_name in enron_data:
    #print(person_name)
    if enron_data[person_name]["total_payments"] == "NaN":
        tpayc = tpayc + 1
        print("Name: {} with total_payments: {}".format(person_name,enron_data[person_name]["salary"]))
    else:
        count = count + 1
print("Number of persons without payment information: {} this is {}% of all {} persons".format(tpayc, round((1.0/(tpayc+count)*tpayc*100),2),(tpayc+count)))
print("#### END Lesson 6-29")

#total_payments@Pois 6-30
tpayc = 0
count = 0
for person_name in enron_data:
    if enron_data[person_name]["poi"]:
        if enron_data[person_name]["total_payments"] == "NaN":
            tpayc = tpayc + 1
            print("Name: {} with total_payments: {}".format(person_name,enron_data[person_name]["salary"]))
        else:
            count = count + 1
print("Number of poi persons without payment information: {} this is {}% of all {} persons".format(tpayc, round((1.0/(tpayc+count)*tpayc*100),2),(tpayc+count)))
print("#### END Lesson 6-23")