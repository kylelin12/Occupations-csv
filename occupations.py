import csv
import random

# Creates a list from the input csv file
occ_list = csv.reader(open('occupations.csv', 'r'))

# Function that converts a list to a dictionary
occ_dic = dict(occ_list)

# Removes the unnecessary header
occ_dic.pop("Job Class")

# Converts the value to a float (stored as a number)
dict((key, float(value)) for key, value in occ_dic.iteritems())

# Prints to double check if everything went according to plan
print occ_dic

#def percent_chance(dictionary):
 #   total_chance = 