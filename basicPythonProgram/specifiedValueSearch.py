"""
   * author - sandeep raj
   * date - 03/11/2020
   * time - 08:58
   * Title -"Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False"
"""

try:

    def is_group_member(list, n):
        for value in list:
            if n == value:
                return True
        return False
    print(is_group_member([1, 5, 8, 3], 3))
    print(is_group_member([5, 8, 3], -1))
except:
    print("check your list data and searching value")
