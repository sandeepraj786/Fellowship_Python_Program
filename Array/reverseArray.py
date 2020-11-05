"""
author -sandeep raj
date -05-11-2020
time -08:56
package -array
problem Statement-Write a Python program to reverse the order of the items in the array.
"""
class ReverseArray:


#create method to reverse an array
    def reverseArray(self,arrOfNum):
        '''
                      :param:self
                      :param:arrOfNum
                      :return:
                     '''
        print("Original array: " + str(arrOfNum))
        arrOfNum.reverse()
        print("Reverse array: " + str(arrOfNum))
    #create an object
arr = ReverseArray()
rangeVal = int(input("Enter The range of an array: "))
arrOfNum = []
for i in range(rangeVal):
    val = int(input("Enter The value for array : "))
    arrOfNum.append(val)
arr.reverseArray(arrOfNum)