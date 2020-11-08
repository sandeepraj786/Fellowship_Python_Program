"""
author -sandeep raj
date -08-11-2020
time -15:03
package -List
problem Statement-' Write a Python function that takes two lists and returns True if they have at
least one common member.'

"""

class CommonMember:
    def checkCommon(self,list1,list2):
        result=False

        for i in list1:
            for j in list2:
                if i==j:
                    result=True
                    return result




list1=[]
try:
    a=int(input("Enter the no of element of 1st list: "))
    for i in range(a):
        value=input("Enter the element of list")
        list1.append(value)

    list2=[]
    a=int(input("Enter the no of element od 2nd list: "))
    for i in range(a):
        value=input("Enter the element of list")
        list2.append(value)

    print(list1,list2)
except:
    print("CHECK YOU INPUT")


if __name__ == '__main__':
    commonMember=CommonMember()
    print(commonMember.checkCommon(list1,list2))


