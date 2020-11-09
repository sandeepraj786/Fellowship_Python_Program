"""
author -sandeep raj
date -09-11-2020
time -03:22
package -Tuple
problem Statement-'Write a Python program to reverse a tuple..'

"""


class ReverseTuple:

    def Reverse(self,tuples):
        new_tup = tuples[::-1]
        return new_tup

rangeVal=int(input("Enter the no of element of tuple: "))
tuple_value=()
for i in range(rangeVal):
    value=input("Enter the element: ")
    tuple_value=tuple_value[:i]+(value,)+tuple_value[:i-1]
print("original Tuple")
print(tuple_value)
print()


if __name__ == '__main__':
    reverseTuple=ReverseTuple()
    print("Reverse Tuple")
    print(reverseTuple.Reverse(tuple_value))



