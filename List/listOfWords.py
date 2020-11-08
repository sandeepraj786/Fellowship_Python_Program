"""
author -sandeep raj
date -08-11-2020
time -12:47
package -List
problem Statement-'Write a Python program to find the list of words that are longer than n from a given list of words.'

"""

class FindList:

    def long_words(self,n, str):
        """

        :param n:
        :param str:
        :return:
        """

        txt = str.split(" ")
        for x in txt:
            if len(x) > n:
                word_len.append(x)
        return word_len

word_len = []
try:
    n=int(input("Enter the no words: "))
    str=input("Enter the list of words: ")
except:
    print("CHECK YOIR INPUT")
if __name__ == '__main__':

    findList=FindList()
    list_of_words=findList.long_words(n,str)
    print(list_of_words)


