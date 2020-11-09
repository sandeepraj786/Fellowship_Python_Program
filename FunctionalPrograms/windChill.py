
"""
author -sandeep raj
date -10-11-2020
time -02:29
package -FunctionalPrograms
problem Statement-'Write a program WindChill.java that takes two double command-line arguments t
and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
National Weather Service defines the effective temperature (the wind chill) to be:

Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger
than 120 or less than 3 (you may assume that the values you get are in that range).
"""



import math
class WindChill:

    def WindChill(self,temp, velocity):
        """
        :param temp: temp input is taken
        :param velocity:  velocity input is taken
        """
        power = math.pow(velocity, 0.6)
        windChill= 35.47 + 0.6215 * temp + (0.4275 * temp + 35.75) * power
        print("Wind Chill of weather")
        print(windChill)




if __name__ == '__main__':
        try:
            temp = int(input("enter temp below 50 in fahrenheit : "))
            velocity = int(input("enter velocity in range of 3m/s and  120m/s : "))
            wind_chill=WindChill()
            wind_chill.WindChill(temp, velocity)

        except ValueError:
                print("check the input")