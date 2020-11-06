"""
author -sandeep raj
date -06-11-2020
time -01:38
package -Sets
problem Statement-'Write a Python program to find maximum and the minimum value in a set'

"""
class SetMaxMin:

    def findMaxMin(self):
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

            print("set element")
            print(a)
            # Find maximum value
            print("maximum value of set")
            print(max(set(a)))
            print("minimum value of set")
            print(min(set(a)))


        except:
            print("provide the currect input")

a=set()
b=SetMaxMin()
b.findMaxMin()

