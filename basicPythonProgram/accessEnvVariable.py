"""
   * author - sandeep raj
   * date - 03/11/2020
   * time - 10:38
   * problem statement -"Write a python program to access environment variables.."
"""
import os
try:
    print("Access all environment variables:")
    print('*----------------------------------*')

    print(os.environ)
    print('*----------------------------------*')

    print("Access a particular environment variable:")
    print(os.environ['PATH'])
    print('*----------------------------------*')

    print('Value of the environment variable key:')
    print(os.getenv('JAVA_HOME'))
    print(os.getenv('PYTHONPATH'))
except:
    print("check the key to access environment variable")





