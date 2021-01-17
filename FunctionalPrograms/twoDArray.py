"""
author -sandeep raj
date -10-11-2020
time -00:20
package -BaicCorePrograms
problem Statement-'2D Array
a. Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
b. I/P -> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner Class
c. Logic -> create 2 dimensional array in memory to read in M rows and N cols
d. O/P -> Print function to print 2 Dimensional Array. In Java use PrintWriter with
OutputStreamWriter to print the output to the screen..
"""

import numpy as np
# array function is used to complete the task
class Matrix:

    # array function is created
    def twoDArray(self, row, col):
        """
              :param row: no of row
              :param col: no of col
              :return: array output
          """
        try:  # try is used for locating the error
            array = [[[np.random.randint(0, 10)] for i in range(row)] for j in range(col)]  # array is created by this
            # function
            print(array)
            return array  # array is returned
        except IndexError:
            print("index error please check ")

if __name__ == "__main__":
    row = int(input("number of rows : "))
    col = int(input("number of coloumn : "))
    matrix=Matrix()
    matrix.twoDArray(row,col)


