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
#print occ_dic_float

# Defines a new function that takes an argument
def percent_chance(dictionary):
    occ_dic_float.pop("Total") # Removes the now unnecessary footer of the csv
    while True:
        for key, value in dictionary.items(): # For loop that goes through each value for each key in the dictionary
            #print chance
            ran_num = random.random() * 99.8 # Generates a random number between [0, 1) * total chance.
            #print ran_num
            if ran_num <= value:
                #print key
                return key


print "\nYour randomly (weighted) occupation is: " + percent_chance(occ_dic_float)