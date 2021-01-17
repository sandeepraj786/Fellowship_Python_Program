"""
author -sandeep raj
date -10-11-2020
time -01:14
package -FunctionalPrograms
problem Statement-'Write a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
"""

import math
class Distance:

    # Distance is used for finding distance between 2 points
    def distance(self,x, y):
        """
        :param x: point 1
        :param y: point 2
        :return:  distance between 2 point
        """
        dist = math.sqrt((x ** 2 + y ** 2))
        print(dist)
        # here difference is returned
        return dist
if __name__ == '__main__':
        try:
            x = int(input("enter num 1 : "))
            y = int(input("enter num 2 : "))
            distance=Distance()
            distance.distance(x,y)

        except ValueError:
            print("check the input ")