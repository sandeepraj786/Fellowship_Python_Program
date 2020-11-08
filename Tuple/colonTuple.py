"""
author -sandeep raj
date -09-11-2020
time -02:00
package -Tuple
problem Statement-'Write a Python program to create the colon of a tuple..'

"""

from copy import deepcopy
class CreateColon:

    #Create method colon of a tuple
    def createColon(self,intVal,floatVal,emptyList,strVal,boolVal):

        tupleValue = (intVal, floatVal, emptyList, strVal, boolVal)
        print("Tuple Data : ", tupleValue)
        print()
        tuplex_colon = deepcopy(tupleValue)

        tuplex_colon[2].append(6)
        print("Copied Tuple : ",tuplex_colon)

create_colon = CreateColon()
intVal = int(input("Enter The Int Value : "))
floatVal = float(input("Enter The Float Value : "))

emptyList = []
strVal = input("Enter A String  : ")
boolVal = bool(input("Enter The Boolean Value True or False : "))

create_colon.createColon(intVal,floatVal,emptyList,strVal,boolVal)