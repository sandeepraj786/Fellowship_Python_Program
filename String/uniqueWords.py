"""
author -sandeep raj
date -09-11-2020
time -17:40
package -String
problem Statement-'Write a Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red.
"""

class UniqueWords:
    def findUnique(self,item):
        words = [word for word in items.split(",")]
        print(",".join(sorted(list(set(words)))))


if __name__ == '__main__':
    unique_word=UniqueWords()
    try:
        items = input("Input comma separated sequence of words: ")
        unique_word.findUnique(items)
    except:
        print("CHECK YOUR INPUT ")



