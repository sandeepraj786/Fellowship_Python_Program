"""
author - sandeep raj
date - 04/11/2020
time - 22:51
problem statement -"Write a Python function to find the maximum and minimum numbers from a sequence of numbers."
"""
try:
    def max_min(data):

      l = data[0]
      s = data[0]
      for num in data:
        if num> l:
          l = num
        elif num< s:
            s = num
      return l, s

    print(max_min([12,32,54,11,98,123,-87,43]))
except:
    print("provide a valid data")