"""
author -sandeep raj
date -08-11-2020
time -12:47
package -List
problem Statement-'Write a Python program to clone or copy a list..'

"""

class CopyList:

    #create method createCopy
    def createCopy(self,ListOfNum):

        """

        :param ListOfNum:
        :return:
        """
        copy_list = list(ListOfNum)
        print("Original list : ",ListOfNum)
        print("Copy list : ",copy_list)


listOfNum=[]
try:
    rangeValue=int(input("Enter the no of element in list: "))
    for i in range(rangeValue):
        value=input("Enter the element of list: ")
        listOfNum.append(value)
except:
    print("CHECK YOUR INPUT")

if __name__ == '__main__':
    copyList=CopyList()
    copyList.createCopy(listOfNum)