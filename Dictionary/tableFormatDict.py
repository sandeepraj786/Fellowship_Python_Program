"""
author -sandeep raj
date -06-11-2020
time -10:26
package -Dictionary
problem Statement-'Write a Python program to print a dictionary in table format.'
"""

# Define the dictionary




# Insert data into dicitonary
dict1 = {1: ["Samuel", 21, 'Data Structures'],
         2: ["Richie", 20, 'Machine Learning'],
         3: ["Lauren", 21, 'OOPS with java'],
         }

# Print the names of the columns.
print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))

# print each data item. 
for key, value in dict1.items():
    name, age, course = value
    print("{:<10} {:<10} {:<10}".format(name, age, course))




