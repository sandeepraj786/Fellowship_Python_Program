"""
author -sandeep raj
date -08-11-2020
time -12:47
package -List
problem Statement-'Write a Python program to remove duplicates from a list.'

"""


class RemoveDuplicate:
    def removeDuplicate(self,list_num):
        """

        :param list_num:
        :return:
        """

        print(set(list_num))

list_num=[]
try:
    range_value=int(input("enter the no of element in list: "))
    for i in range(range_value):
        value=input("Enter the element of list: ")
        list_num.append(value)
    print(list_num)
except:
    print("CHECK YOU INPUT")

if __name__ == '__main__':
    remove_douplicate=  RemoveDuplicate()
    remove_douplicate.removeDuplicate(list_num)

