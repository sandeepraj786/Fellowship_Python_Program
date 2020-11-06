"""
author -sandeep raj
date -06-11-2020
time -20:13
package -Dictionary
problem Statement-'Write a Python program to convert a list into a nested dictionary of keys'
"""

num_list = ['sandeep', 'lion', 'burjKhlifa', 'Modi']
try:
    new_dict = current = {}
    for name in num_list:
        current[name] = {}
        current = current[name]
    print(new_dict)
except:
    print("check the input my list")
