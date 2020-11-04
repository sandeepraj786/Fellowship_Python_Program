"""
author - sandeep raj
date - 03/11/2020
time - 17:42
problem statement -"Write a program to get execution time for a Python method."
"""

import time
try:
    def sum_of_n_numbers(n):
        start_time = time.time()
        s = 0
        for i in range(1,n+1):
            s = s + i
        end_time = time.time()
        return s,end_time-start_time

    n = 5
    print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))
except:
    print("Enter a interger number")