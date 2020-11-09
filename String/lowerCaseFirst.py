"""
author -sandeep raj
date -09-11-2020
time -18:10
package -String
problem Statement-'Write a Python program to lowercase first n characters in a string..
"""



class FirstNLowerCase:
    def lowerCase(self,str1,n):

        """

        :param str1:
        :param n:

        """

        print(str1[:n].lower() + str1[n:])


if __name__ == '__main__':
    first_n_lowerCase=FirstNLowerCase()
try:
    str=input("Enter the string in Capital letter: ")
    n=int(input("enter the number at which change to lower case: "))
    first_n_lowerCase.lowerCase(str,n)

except:
    print("PLEASE PROVIDE CORRECT INPUT")

