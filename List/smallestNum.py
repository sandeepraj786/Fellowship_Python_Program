"""
author -sandeep raj
date -08-11-2020
time -10:51
package -List
problem Statement-'Write a Python program to get the smallest number from a list.'

"""

class MinListItems:



    # find the minimum value
    def findMin(self,ListOfNum):
        """

        :param ListOfNum:
        :return:
        """
        min = ListOfNum[0]
        for x in ListOfNum:
            if x < min:
                min = x
        print("Smallest Number in List Items is : ",min)
try :

    rangeVal = int(input("Enter The range of value you want to enter : "))
    ListOfNum = [ ]
    for i in range(rangeVal):
        val = int(input("Enter The value for List : "))
        ListOfNum.append(val)
    print("List Data :- ",ListOfNum)
except:
    print('CHECK YOUR INPUT')
if __name__=="__main__":
        list_of_data=MinListItems()
        list_of_data.findMin(ListOfNum)




