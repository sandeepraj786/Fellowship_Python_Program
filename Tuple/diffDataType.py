"""
author -sandeep raj
date -09-11-2020
time -01:38
package -Tuple
problem Statement-'Write a Python program to create a tuple with different data types.'

"""
class DiffDateType:

    #create method for different datatype
    def createDiffType(self,intVal,floatVal,strVal,boolVal):
        '''
        :param:ListOfNum: Clone the element in list

        '''
        tupleValue = (intVal, floatVal, strVal, boolVal)
        print("Tuple Data :- ", tupleValue)
try:
    tupleData = DiffDateType()
    intVal = int(input("Enter The Int Value : "))
    floatVal = float(input("Enter The Float Value : "))
    strVal = input("Enter A String  : ")
    boolVal = bool(input("Enter The Boolean Value True or False : "))
    tupleData.createDiffType(intVal,floatVal,strVal,boolVal)
except ValueError:
    print("Enter the correct value")





