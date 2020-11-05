"""
author -sandeep raj
date -05-11-2020
time -10:09
package -array
problem Statement-Write a Python program to remove the first occurrence of a specified element from an
array.
"""
class RemoveOccurence:
    #method to remove occurence
    def removeOccurence(self,arrOfNUm,value):
        print("Original array: " + str(arrOfNum))
        arrOfNum.remove(value)
        print("Number of occurrences of the number ",value," in array: " + str(arrOfNUm.count(value)))
        print("Updated array: " + str(arrOfNum))

   #creaing an object
arr = RemoveOccurence()

rangeVal = int(input("Enter the no of element of an array : "))
arrOfNum = []
for i in range(rangeVal):
    val = int(input("Enter The value for array : "))
    arrOfNum.append(val)
Value = int(input("Enter The Value You Want To Remove : "))
arr.removeOccurence(arrOfNum,Value)