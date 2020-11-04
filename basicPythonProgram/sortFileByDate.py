"""
author - sandeep raj
date - 04/11/2020
time - 08:51
problem statement-"  Write a Python program to sort files by date."
"""
import glob
import os
try:
 files = glob.glob("*.txt")
 files.sort(key=os.path.getmtime)
 print("\n".join(files))
except:
    print("EnterProperFileExtension")