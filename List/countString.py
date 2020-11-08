"""
author -sandeep raj
date -08-11-2020
time -11:25
package -List
problem Statement-'Write a Python program to count the number of strings where the string length is 2 or
more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2''''

"""

class CountString:

    #Create method to count the ring
    def matchCharacter(self,listOfStr):

        """

        :param listOfStr:
        :return:
        """
        countStr = 0
        for Str in listOfStr:
            if len(Str) >= 2 and Str[0] == Str[-1]:
                countStr += 1
        print("The String Count Whos First And Last Char Is Same Are : ",countStr)
try :
    rangeVal = int(input("Enter The range of value you want to enter : "))
    listOfStr = [ ]
    for i in range(1,rangeVal+1):
        val = input("Enter The value for List in Strings : ")
        listOfStr.append(val)
    print("List : ",listOfStr)
except ValueError:
    print("PROVIDE TO PROPER INPUT")


if __name__=="__main__":
        list_of_data=CountString()
        list_of_data.matchCharacter(listOfStr)


