"""
author -sandeep raj
date -08-11-2020
time -15:36
package -List
problem Statement-'Write a Python program to print a specified list after removing the 0th, 4th and
5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']'

"""

class RemoveElement:

    def reomove(self,list1,pos):
        """

        :param list1:
        :param pos:

        """
        new_list=[]
        for x in range(len(list1)):
            if x!=pos:
                new_list.append(list1[x])
        print(new_list)


list1=[]
try:
    n=int(input("enter the number of list element: "))
    for i in range(n):
        value=input("Enter the element of list: ")
        list1.append(value)
    print(list1)
    pos=int(input("Enter the index you want to remove"))
except:
    print("CHECK YOUR INPUT")

if __name__ == '__main__':
    removeElement=RemoveElement()
    removeElement.reomove(list1,pos)