"""
author -sandeep raj
date -05-11-2020
time -10:28
package -Dictionary
problem Statement-Write a Python script to sort (ascending and descending) a dictionary by
value.
"""

import operator
class DictionaySort:
    #create a method fot sorting purpose
    def findAscDesc(self, dictOfNum):
        '''
                       :param:self
                       :param:dictOfNum
                       :return:
                       '''
        print('Original dictionary : ', dictOfNum)
        sortedAsc = dict(sorted(dictOfNum.items(), key=operator.itemgetter(1)))
        print('Dictionary in ascending order by value : ', sortedAsc)
        sortedDesc = dict(sorted(dictOfNum.items(), key=operator.itemgetter(1), reverse=True))
        print('Dictionary in descending order by value : ', sortedDesc)

#creating an object
dictionary = DictionaySort()
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = { }
for i in range(1,rangeVal+1):
    val = int(input("Enter The value for array : "))
    dictOfNum.setdefault(i, val)
dictionary.findAscDesc(dictOfNum)