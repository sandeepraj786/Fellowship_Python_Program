"""
author -sandeep raj
date -09-11-2020
time -03:09
package -String
problem Statement-'Write a Python program to count the number of characters (character frequency) in a
string.
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}'''.'

"""

class CountNumber:

    def char_frequency(self,str1):
        """

        :param str1:
        :return: dict
        """

        dict = {}
        for n in str1:
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
        return dict

if __name__ == '__main__':
    str=input("Enter the string : ")
    count_number=CountNumber()
    print(count_number.char_frequency(str))