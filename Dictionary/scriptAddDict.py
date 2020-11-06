"""
author -sandeep raj
date -06-11-2020
time -09:22
package -Dictionary
problem Statement-'Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}.
"""
class DictKeyAdd:
    def addKey(self, dictOfNum,key,value):
        print(dictOfNum)
        dictOfNum.update({key: value})
        print(dictOfNum)
'''
    :param self:
    :param dictOfNum:
    :param key:
    :param value:
    '''
dictionary = DictKeyAdd()
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = { }
for i in range(1,rangeVal+1):
    val = int(input("Enter The value for dictionary : "))
    dictOfNum.setdefault(i, val)
key = int(input("Enter The Key In Which You Want To Add The Value : "))
value = int(input("Enter The Value : "))
dictionary.addKey(dictOfNum,key,value)