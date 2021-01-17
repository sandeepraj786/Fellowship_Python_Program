"""
author -sandeep raj
date -09-11-2020
time -23:27
package -BaicCorePrograms
problem Statement-'Leap Year
a. I/P -> Year, ensure it is a 4 digit number.
b. Logic -> Determine if it is a Leap Year.
c. O/P -> Print the year is a Leap Year or not.
"""

class LeapYear:
   def leapyear(self):
    year=int(input('enter year'))
    if year%100==0: #century year
       if year%400==0:
           print ('{} is leap year'.format(year))
       else:
          print ('{} is not leap year'.format(year))
    else:
       if year%4==0:
          print ('{} is leap year'.format(year))
       else:
         print ('{} is not leap year'.format(year))
if __name__=='__main__':
        obj=LeapYear()
        obj.leapyear()
