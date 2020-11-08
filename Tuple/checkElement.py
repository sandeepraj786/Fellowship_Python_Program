"""
author -sandeep raj
date -09-11-2020
time -02:50
package -Tuple
problem Statement-'Write a Python program to check whether an element exists within a tuple.'

"""

class CheckElement:
    def checkElement(self):
        try:

            rangeVal = int(input("Enter The no of element in tuple : "))
            tupleValue = ( )
            for i in range(rangeVal):
                val = int(input("Enter The Int value for tuple : "))
                tupleValue = tupleValue[: i] + (val,) + tupleValue[i:]
            print(tupleValue)

            element = input("which element do you want to check: ")
            print(element in tupleValue)
        except:
            print("CHECK YOUR INPUT")


if __name__ == '__main__':

    check_element=CheckElement()
    check_element.checkElement()



