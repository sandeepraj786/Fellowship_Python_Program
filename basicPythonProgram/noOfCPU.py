"""
   * author - sandeep raj
   * date - 03/11/2020
   * time - 10:25
   * Title -"Write a Python program to find out the number of CPUs using."
"""
import multiprocessing
try:
 print(multiprocessing.cpu_count())
except:
    print("in this system number of CPU is not recognized")