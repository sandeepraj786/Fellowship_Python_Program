"""
author - sandeep raj
date - 04/11/2020
time - 22:04
problem statement -"Write a Python program to empty a variable without destroying it."
"""

str1='122.22'
try:
    print("Original String: ",str1)
    print("\nAdded trailing zeros:")
    str1 = str1.ljust(8, '0')
    print(str1)
    str1 = str1.ljust(10, '0')
    print(str1)
    print("\nAdded leading zeros:")
    str1='122.22'
    str1 = str1.rjust(8, '0')
    print(str1)
    str1 = str1.rjust(10, '0')
    print(str1)
except:
    print("enter a valid string")