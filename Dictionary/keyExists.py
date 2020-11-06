"""
author -sandeep raj
date -06-11-2020
time -20:04
package -Dictionary
problem Statement-'Write a Python program to check multiple keys exists in a dictionary.'
"""

class CheckKey:

    student = {
      'name': 'Alex',
      'class': 'V',
      'roll_id': '2'
    }
    try:
        print(student.keys() >= {'class', 'name'})
        print(student.keys() >= {'name', 'Alex'})
        print(student.keys() >= {'roll_id', 'name'})
    except:
        print("check yor key and value pair")



