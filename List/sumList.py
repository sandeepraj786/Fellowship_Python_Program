"""
author -sandeep raj
date -06-11-2020
time -02:07
package -List
problem Statement-'Write a Python program to sum all the items in a list.'

"""

def sum_list(items):
    """

    :param items:
    :return:
    """
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([65,87,43]))