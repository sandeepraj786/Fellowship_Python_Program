"""
author - sandeep raj
date - 04/11/2020
time - 22:27
problem statement -"Write a Python program to convert an integer to binary keep leading zeros."
"""

x = 50
try:
    print(format(x, '08b'))
    print(format(x, '010b'))
except:
    print("provide a valid input integer")