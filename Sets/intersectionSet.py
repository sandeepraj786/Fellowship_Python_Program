"""
author -sandeep raj
date -06-11-2020
time -00:18
package -Sets
problem Statement-'Write a Python program to create an intersection of sets.'

"""
class CreateIntersection:

    #create method to intersection
    def intersection(self,firstSetValue,SecondSetValue):
        '''
        :param:firstSetvalue pass the first value
        :param:SecondSetValue pass the second value
        :return : return the insection value
                     '''
        intersectionSet = firstSetValue & SecondSetValue
        print(intersectionSet)


firstSetValue = set()
rangeVal = int(input("Enter The Range Of Values You Want To Enter In First Set: "))
for i in range(rangeVal):
    valAddFirst = input("Enter The String Or Value : ")
    firstSetValue.add(valAddFirst)

SecondSetValue = set()
rangeVal = int(input("Enter The Range Of Values You Want To Enter In second Set: "))
for i in range(rangeVal):
    valAddSecond = input("Enter The String Or Value : ")
    SecondSetValue.add(valAddSecond)

print("Data Set First: ",firstSetValue)
print("Data Set Second: ",SecondSetValue)


setMembers = CreateIntersection()
setMembers.intersection(firstSetValue,SecondSetValue)