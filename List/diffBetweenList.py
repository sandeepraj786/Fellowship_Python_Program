"""
author -sandeep raj
date -08-11-2020
time -15:36
package -List
problem Statement-'Write a Python program to get the difference between the two lists.'

"""
from utilityPackage import Ulility

class DiffBWList:

    def Diff(self,x,y):
        """

        :param x:
        :param y:
        :return:
        """

        return (list(list(set(x) - set(y)) + list(set(y) - set(x))))


if __name__ == '__main__':

    #calling createList method
     a= Ulility.createList()
     b=Ulility.createList()
print()

#creatimg an object
diff_list=DiffBWList()
#calling Diff method
result=diff_list.Diff(a,b)
print("Difference b/w two list : ", result)

















