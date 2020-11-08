"""
author -sandeep raj
date -08-11-2020
time -23:52
package -List
problem Statement-'Write a Python program to find common items from two lists'

"""
from utilityPackage import  Ulility
class CommonItems:
    # in two lists
    def common_member(self,a, b):
        """

        :param a:
        :param b:

        """
        a_set = set(a)
        b_set = set(b)

        if (a_set & b_set):
            print(a_set & b_set)
        else:
            print("No common elements")

if __name__ == '__main__':
    x=Ulility.createList()
    y=Ulility.createList()
    common_item = CommonItems()
    common_item.common_member(x,y)


