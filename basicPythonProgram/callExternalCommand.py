"""
   * author - sandeep raj
   * date - 03/11/2020
   * time - 10:12
   * Title -"Write a python program to call an external command in Python."
"""
try:
 from subprocess import call
 call(["ls", "-l"])
except:
    print("EnterProperExternalCommand")


  