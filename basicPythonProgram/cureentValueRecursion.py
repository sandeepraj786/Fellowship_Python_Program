"""
author - sandeep raj
date - 04/11/2020
time - 09:40
problem statement -"Write a Python program to get the current value of the recursion limit."
"""
import sys
try:
 print()
 print("Current value of the recursion limit:")
 print(sys.getrecursionlimit())
 print()
except:
    print("checkedImportStatementAndInbuiltMethod")