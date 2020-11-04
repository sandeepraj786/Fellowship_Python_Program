"""
author - sandeep raj
date - 04/11/2020
time - 22:27
problem statement -"Write a Python program to extract single key-value pair of a dictionary in variables."
"""

d = {'Sandeep': 'DevOps'}
try:
    (c1, c2), = d.items()
    print(c1)
    print(c2)
except:
    print("provide valid dictionary")