"""
   * author - sandeep raj
   * date - 03/11/2020
   * time - 10:38
   * Title -"Write a Python program to list all files in a directory in Python."
"""
from os import listdir
from os.path import isfile, join
try:
    files_list = [f for f in listdir (r'C:\Users\hp') if isfile(join(r'C:\Users\hp', f))]
    print(files_list);
except:
    print("provide a proper path")
