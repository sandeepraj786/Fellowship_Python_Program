"""
   * author - sandeep raj
   * date - 03/11/2020
   * time - 08:42
   * Title -"Write a Python program to create a histogram from a given list of integers"
"""
try:

    def histogram( list ):
        for n in list:
            output = ''
            times = n
            while( times > 0 ):
              output += '*'
              times = times - 1
            print(output)

    histogram([4, 5, 7, 4])
except:
    print("Invalid input of list")