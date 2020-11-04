"""
author - sandeep raj
date - 04/11/2020
time - 09:11
problem statement -"Write a Python program to get the size of an object in bytes."
"""
import sys


first_string = "Hello"
second_string = "My name "
third_string = "is Sandeep"
print()
try:
    print("Memory size of '" + first_string + "' = " + str(sys.getsizeof(first_string)) + " bytes")
    print("Memory size of '" + second_string + "' = " + str(sys.getsizeof(second_string)) + " bytes")
    print("Memory size of '" + third_string+ "' = " + str(sys.getsizeof(third_string)) + " bytes")
    print()
except:
    print("ProvideProperObjectAndCheckedInBuiltMethod")