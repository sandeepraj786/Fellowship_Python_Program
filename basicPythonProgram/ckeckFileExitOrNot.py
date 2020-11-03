"""
   * author - sandeep raj
   * date - 03/11/2020
   * time - 09:50
   * Title -"Write a Python program to check whether a file exists."
"""



import pathlib
try:

    file = pathlib.Path("xyz.txt")
    if file.exists():
        print("File exist")
    else:
        print("File not exist")
except:
    print("please provide a correct file format")