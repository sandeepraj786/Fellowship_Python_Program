"""
author -sandeep raj
date -06-11-2020
time -23:15
package -Sets
problem Statement-'Write a Python program to remove item(s) from set'

"""
class RemoveItem:

    def removeItem(self):
        '''
        removeItem method to remove the particular item from the set
        :param: self
        :return:
        '''
        try:
            n = int(input("Enter the no of item in a set: "))
            for i in range(n):
                value = input("Enter the element of set: ")
                a.add(value)
            print(a)
            remove_item = input("which element you want to remove: ")
            a.remove(remove_item)
            print(a)
        except:
            print("provide the currect input")

a=set()
b=RemoveItem()
b.removeItem()













