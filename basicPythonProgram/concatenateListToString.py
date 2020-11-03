"""
   * author - sandeep raj
   * date - 03/11/2020
   * time - 08:42
   * Title -"Write a Python program to concatenate all elements in a list into a string and return it."
"""

def concatenate_list_element(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_element([12, 4, 9, 32]))