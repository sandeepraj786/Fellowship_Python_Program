"""
author -sandeep raj
date -09-11-2020
time -03:05
package -Tuple
problem Statement-'Write a Python program to convert a list to a tuple.'

"""

class ListToTuple:

    #Create method checkTuple
    def toTuple(self,ListOfNum):
        """
                          :param ListOfNum: element the value
                          :return: tuple value
                         """
        tupleOfNum = tuple(ListOfNum)
        print("Tuple Data : ",tupleOfNum)
listData = ListToTuple()
rangeVal = int(input("Enter The range of value you want to enter : "))
ListOfNum = [ ]
for i in range(rangeVal):
    val = int(input("Enter The value for tuple : "))
    ListOfNum.append(val)

print("List Data :- ",ListOfNum)
listData.toTuple(ListOfNum)