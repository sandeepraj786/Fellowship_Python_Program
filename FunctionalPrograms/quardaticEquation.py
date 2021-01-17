
"""
author -sandeep raj
date -10-11-2020
time -01:50
package -FunctionalPrograms
problem Statement-'Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
can be found using a formula (Note: Take a, b and c as input values)
delta = b*b - 4*a*c
Root 1 of x = (-b + sqrt(delta))/(2*a)
Root 2 of x = (-b - sqrt(delta))/(2*a)
"""


import math

class Quardatic:



    def findRoots(self,a, b, c):
        # If a is 0, then equation is
        # not quadratic, but linear
        if a == 0:
            print("Invalid")
            return -1
        d = b * b - 4 * a * c
        sqrt_val = math.sqrt(abs(d))

        if d > 0:
            print("Roots are real and different ")
            print((-b + sqrt_val) / (2 * a))
            print((-b - sqrt_val) / (2 * a))
        elif d == 0:
            print("Roots are real and same")
            print(-b / (2 * a))
        else:  # d<0
            print("Roots are complex")
            print(- b / (2 * a), " + i", sqrt_val)
            print(- b / (2 * a), " - i", sqrt_val)



if __name__ == '__main__':

    a = int(input("Enter the Integer: "))
    b = int(input("Enter the Integer: "))
    c = int(input("Enter the Integer: "))

# Function call
quardatic=Quardatic()
quardatic.findRoots(a,b,c)


