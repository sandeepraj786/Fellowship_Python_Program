
"""
   * author - sandeep raj
   * date - 02/11/2020
   * time - 16:58
   * Title -"Write a Python program to print the calendar of a given month and year."
"""
try:

    import calendar
    YEAR=int(input("Enter the Year : "))
    MONTH=int(input("Enter the Month : "))
    print(calendar.month(YEAR,MONTH))
except:
    print("enter a valid year and month")