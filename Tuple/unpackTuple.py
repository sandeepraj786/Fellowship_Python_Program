"""
author -sandeep raj
date -09-11-2020
time -01:56
package -Tuple
problem Statement-'Write a Python program to unpack a tuple in several variables..'

"""


# function takes normal arguments
# and multiply them
def result(x, y):
    return x * y


# function with normal variables
print(result(10, 100))

# A tuple is created
z = (10, 100)

# Tuple is passed
# function unpacked them

print(result(*z))