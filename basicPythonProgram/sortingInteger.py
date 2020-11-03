"""
author - sandeep raj
date - 03/11/2020
time - 19:12
problem statement -"Write a Python program to sort three integers without using conditional statements and
loops."
"""
try:
    #Three input integer number
 first_number = int(input("Enter first number: "))
 second_number = int(input("Enter second number: "))
 third_number = int(input("Enter third number: "))

#using method max and min
 min_number = min(first_number, second_number, third_number)
 max_number = max(first_number, second_number, third_number)
 MiddleNumber = (first_number + second_number + third_number) - min_number  - max_number
 print("Sorted order Of Numbers are : ",min_number, MiddleNumber, max_number)
except:
    print("EnterValidIntegerNumber")
