"""
author - sandeep raj
date - 03/11/2020
time - 16:50
problem statement-" Write a Python program to get the current username"
"""
import getpass
try:
 print(getpass.getuser())
except:
    print("use Correct Inbuilt Method")