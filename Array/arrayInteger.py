"""
author -sandeep raj
date -05-11-2020
time -08:56
package -array
problem Statement-Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
"""
from utility import Utillity
class ArrayOfIntegers:
    def findIndex(self,arrayNum,indexValue):
        '''
        findIndex method is taking two variable as an agument and displaying array element and first three itom index
               :param:self
               :param:arrayNum
               :param:indexValue
              '''
        print(arrOfNum)
        print("Access first three items individually")
        print("Searched Index Element : ",arrayNum[indexValue])
        print("Last Element : ", arrayNum[-1])
        print("First Element :", arrayNum[0])
arr = ArrayOfIntegers()
arrOfNum = []
print("****range of array element****")
n=Utillity.inputFunction()
for i in range(n):
    print("*****array element***")
    val = Utillity.inputFunction()
    arrOfNum.append(val)
print("*****index value you want****")
indexValue = Utillity.inputFunction()
arr.findIndex(arrOfNum,indexValue)



