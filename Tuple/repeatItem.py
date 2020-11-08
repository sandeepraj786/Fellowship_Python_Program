"""
author -sandeep raj
date -09-11-2020
time -02:21
package -Tuple
problem Statement-'write a Python program to find the repeated items of a tuple'

"""

class RepeatedItem:

    #Create Method to count the number
    def findRepetedItem(self,tupleValue,findVal):
        '''
        :param:tupleValue: colection of Tuple Element

        '''
        countValue = tupleValue.count(findVal)
        print("Count Of Value ",findVal,"Is : ",countValue)

try:

    tupleData = RepeatedItem()
    rangeVal = int(input("Enter The range of value you want to enter : "))
    tupleValue = ( )
    for j in range(rangeVal):

       val = int(input("Enter The Int value for tuple : "))
       tupleValue = tupleValue[ : j] + (val,) + tupleValue[ j : ]

    print("Tuple Data :- ", tupleValue)

    findVal = int(input("Enter value you want to Count : "))



    tupleData.findRepetedItem(tupleValue,findVal)
except:
    print("CHECK YOUR INPUT")