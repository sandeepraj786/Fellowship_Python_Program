"""
author -sandeep raj
date -09-11-2020
time -00:54
package -Tuple
problem Statement-'Write a Python program to create a tuple.'

"""

class CreateTuple:

    #Create method
    def create(self,rangeVal):
        """
                        :param rangeVal: element the value
                        :return: tuple value
                       """
        tupleValue = ( )
        for i in range(rangeVal):
            val = int(input("Enter The Int value for tuple : "))
            tupleValue = tupleValue[ : i] + (val,) + tupleValue[ i : ]
        print("Tuple Data :- ", tupleValue)

tupleData = CreateTuple()
rangeVal = int(input("Enter The range of value you want to enter : "))
tupleData.create(rangeVal)