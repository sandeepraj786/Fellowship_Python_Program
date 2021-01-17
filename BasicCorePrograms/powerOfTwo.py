"""
author -sandeep raj
date -09-11-2020
time -23:27
package -BaicCorePrograms
problem Statement-'Power of 2
a. Desc -> This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.
b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
c. Logic -> repeat until i equals N.
d. O/P -> Print the year is a Leap Year or not..
"""

class PowerOfTwo:
    def power(self):

        n = int(input("Enter the number:"))
        for i in range(pow(2, n)):
            print("2 *", i, " = ", (2 * i))
            if ((2 * i) % 400 == 0) or (((2 * i) % 4 == 0) and ((2 * i) % 100 != 0)):
                print("%d is a Leap Year" % (2 * i))
            else:
                print("%d is Not a Leap Year" % (2 * i))



if __name__=='__main__':
    power_of_two=PowerOfTwo()
    power_of_two.power()

