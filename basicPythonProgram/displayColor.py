"""
   * author - sandeep raj
   * date - 02/11/2020
   * time - 16:17
   * Title -"Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]"
"""
try:
    color_list = ["Red","Green","White" ,"Black"]
    print(color_list[0])
    print(color_list[len(color_list)-1])

except:
    print("check index of list")
