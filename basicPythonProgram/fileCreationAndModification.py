"""
author - sandeep raj
date - 03/11/2020
time - 18:55
problem statement -" Write a Python program to get file creation and modification date/times."
"""
import os.path, time
try:
 print("Last modified: %s" % time.ctime(os.path.getmtime("xyz.txt")))
 print("Created: %s" % time.ctime(os.path.getctime("xyz.txt")))
except:
    print("ProvideProperFileName")