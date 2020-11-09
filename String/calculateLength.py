"""
author -sandeep raj
date -09-11-2020
time -03:09
package -String
problem Statement-'Write a Python program to calculate the length of a string..'

"""

class CalulateLength:

    def string_length(self,str1):
        """

        :param str1:
        :return: count
        """
        count = 0
        for char in str1:
            count += 1
        return count


if __name__ == '__main__':
    calulate_length=CalulateLength()
    str=input("Enter the string : ")
    print(calulate_length.string_length(str))