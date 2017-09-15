import csv
import random

# Creates a list from the input csv file
occ_list = csv.reader(open('occupations.csv', 'r'))

# Function that converts a list to a dictionary
occ_dic = dict(occ_list)

# Removes the unnecessary header of the csv
occ_dic.pop("Job Class")


# Converts the value to a float (stored as a number)
occ_dic_float = dict((key, float(value)) for key, value in occ_dic.iteritems())

# Prints to double check if everything went according to plan
print occ_dic_float

# Defines a new function that takes an argument
def percent_chance(dictionary):
    ran_num = random.random() * 100.0 # Generates a random numberq between [0, 1)
    total_chance = occ_dic_float.get("Total") # Sets the total as the one given
    occ_dic_float.pop("Total") # Removes the now unnecessary footer of the csv
    for key, value in dictionary.items(): # For loop that goes through each value for each key in the dictionary
        total_chance += value # Keeps track of the total chance
        if ran_num <= total_chance:
            return key

print "\nYour randomly (weighted) occupation is: " + percent_chance(occ_dic_float)