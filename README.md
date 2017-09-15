# Occupations-csv

In the workshop you will find a .csv file that contains information about occupations in the United States (Courtesy of Mr. Brooks). Each line looks something like this:
 ```
    Legal,0.8
    "Education, training and library",6.1
```
The first item is the name of the occupation and the second is the percentage that occupation makes up of the U.S. workforce. Note that when the occupation has a comma in it, it is surrounded by quotation marks.

Your job (in pairs):

* Read in the file and build an appropriate dictionary from it. Make sure the percentages are stored as numbers.

* Create a function that returns a randomly selected occupation where the results are weighted by the percentage given. For example, there should be a 6.1% chance that "Education, training an library" is returned.

File this under **03_occupation**