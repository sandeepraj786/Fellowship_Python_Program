"""
author -sandeep raj
date -06-11-2020
time -00:25
package -Sets
problem Statement-'Write a Python program to create set difference.'

"""

class SetDifference:

    #create method and find difference
    def difference(self,firstSetValue,SecondSetValue):
        '''
               :param:firstSetvalue pass the first value
               :param:SecondSetValue pass the second value
               :return : return the insection value
        '''
        diffSet = firstSetValue - SecondSetValue
        print("Difference in Set : ",diffSet)

firstSetValue = set()
rangeVal = int(input("Enter The Range Of Values You Want To Enter In First Set: "))
for i in range(rangeVal):
    valAddFirst = input("Enter The element: ")
    firstSetValue.add(valAddFirst)

SecondSetValue = set()
rangeVal = int(input("Enter The Range Of Values You Want To Enter In second Set: "))
for i in range(rangeVal):
    valAddSecond = input("Enter The String Or Value : ")
    SecondSetValue.add(valAddSecond)

print("Data Set First: ",firstSetValue)
print("Data Set Second: ",SecondSetValue)


setMembers = SetDifference()
setMembers.difference(firstSetValue,SecondSetValue)