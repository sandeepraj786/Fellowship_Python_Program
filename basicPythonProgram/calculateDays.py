
"""
   * author - sandeep raj
   * date - 02/11/2020
   * time - 19:38
   * Title -"Write a Python program to calculate number of days between two dates.."
"""
try:

    from datetime import date
    first_date = date(2014, 7, 2)
    last_date = date(2014, 7, 11)
    diff_date = last_date - first_date
    print(diff_date.days)
except:
    print("check first date and last date")
