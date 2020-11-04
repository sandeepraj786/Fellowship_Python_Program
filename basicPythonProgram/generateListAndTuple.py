"""
   * author - sandeep raj
   * date - 02/11/2020
   * time - 14:48
   * Title -"Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers."
"""
try:

    sampleData=(input("Enter a sequence of comma-separated numbers :"))
    list=sampleData.split(",")
    tuple=tuple(list)
    print("List: ", list)
    print("Tuple: ", tuple)
except:
    print("enter a valid number seprated by comma")