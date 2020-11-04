"""
author - sandeep raj
date - 04/11/2020
time - 21:17
problem statement -"Write a Python program to retrieve file properties."
"""
import os.path
import time
try:
 print('File         :', __file__)
 print('Access time  :', time.ctime(os.path.getatime(__file__)))
 print('Modified time:', time.ctime(os.path.getmtime(__file__)))
 print('Change time  :', time.ctime(os.path.getctime(__file__)))
 print('Size         :', os.path.getsize(__file__))
except:
    print("Checked Inbuilt  Function And Import Statements")