"""
author -sandeep raj
date -06-11-2020
time -00:58
package -Sets
problem Statement-'Write a Python program to use of frozensets..'

"""

class SymmenticDifference:

    #create method and find difference
    def symmenticDifference(self,firstSetValue,SecondSetValue):
        '''
               :param:firstSetvalue pass the first value
               :param:SecondSetValue pass the second value
               :return : return
        '''
        # use isdisjoint(). Return True if the set has no elements in common with other.
        print(firstSetValue.isdisjoint(SecondSetValue))
        # use difference(). Return a new set with elements in the set that are not in the others.
        print(firstSetValue.difference(SecondSetValue))
        # new set with elements
        print(firstSetValue | SecondSetValue)

firstSetValue = frozenset([1, 2, 3, 4, 5])
SecondSetValue = frozenset([3, 4, 5, 6, 7])

setMembers = SymmenticDifference()
setMembers.symmenticDifference(firstSetValue,SecondSetValue)