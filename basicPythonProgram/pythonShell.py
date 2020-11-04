"""
author - sandeep raj
date - 04/11/2020
time - 22:43
problem statement -"Write a Python program to determine whether a Python shell is executing in 32bit or 64bit mode on OS?."
"""


# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
print(struct.calcsize("P") * 8)