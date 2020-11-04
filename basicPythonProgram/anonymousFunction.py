"""
author - sandeep raj
date - 04/11/2020
time - 10:33
problem statement -"Get numbers divisible by fifteen from a list using an anonymous function."
"""

num_list = [115, 125, 65, 95, 100, 600, 15]
# use anonymous function to filter
try:
    result = list(filter(lambda x: (x % 15 == 0), num_list))
    print("Numbers divisible by 15 are",result)
except:
    print("provide valid list")