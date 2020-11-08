"""
author -sandeep raj
date -08-11-2020
time -15:36
package -List
problem Statement-'Write a Python program to generate all permutations of a list in Python.'

"""

import itertools
class ListPermutation:

    #this method calculate the permutation
    def getPermutation(self, listOfStr):
        """

        :param listOfStr:
        :return:
        """
        permList = (list(itertools.permutations(list1)))
        return permList


rangeVal = int(input("Enter the no of element in the list : "))
list1 = []
for i in range(rangeVal):
    value = input("Enter The element: ")
    list1.append(value)

listPermutation = ListPermutation()
print("List  : ", list1)
print("The Updated List Are : ", listPermutation.getPermutation(list1))