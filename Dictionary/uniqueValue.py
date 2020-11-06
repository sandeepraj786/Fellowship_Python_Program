"""
author -sandeep raj
date -06-11-2020
time -09:36
package -Dictionary
problem Statement-'Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}'
"""
from utility import Utillity

class UniqueDictionary:

    # This method printing unique value
    def unique(self, dictSet):
        """
                     :param dicSet: this is use for dictionat value
                     :return: Remove the repeating value
                     """
        try:
            print("Dictionary : ", dictSet)
            uniqueValue = set(val for dic in dictSet for val in dic.values())
            print("Unique Dictionary: ", uniqueValue)
        except:
            print("Enter a valid key and value")
dictValue = UniqueDictionary()
print("Enter The range of value you want to enter : ")
rangeVal = Utillity.inputFunction()
dictOfNum = {}
for i in range(1,rangeVal+1):
    key = input("Enter The Key : ")
    val = input("Enter The value for dictionary : ")
    dictOfNum.setdefault(key, val)

dictSet = [dictOfNum]
print(dictSet)
dictValue.unique(dictSet)