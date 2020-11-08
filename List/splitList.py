"""
author -sandeep raj
date -08-11-2020
time -00:22
package -List
problem Statement-'Write a Python program to split a list based on first character of word.'

"""
from utilityPackage import Ulility
from itertools import groupby
from operator import itemgetter

class SplitItem:

    def split(self,word_list):
        """

        :param word_list:

        """

        for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
            print(letter)
            for word in words:
                print(word)




if __name__ == '__main__':
    a=Ulility.createList()
    split_item=SplitItem()
    split_item.split(a)
