"""
author -sandeep raj
date -06-11-2020
time -20:43
package -Dictionary
problem Statement-'Write a Python program to count number of items in a dictionary value that is a list'
"""

dict =  {'sandeep': ['java', 'python', 'c++'], 'raj': ['c programming', 'c#']}
ctr = sum(map(len, dict.values()))
print(ctr)