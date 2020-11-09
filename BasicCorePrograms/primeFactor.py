"""
author -sandeep raj
date -09-11-2020
time -23:9
package -BaicCorePrograms
problem Statement-'Factors
a. Desc -> Computes the prime factorization of N using brute force.
b. I/P -> Number to find the prime factors
c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
d. O/P -> Print the prime factors of number N..
"""

class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass
try:
    number=(int(input("Enter the number: ")))
    if number <= 0:
        raise  ValueTooSmallError
    for i in range(2,number):
        while number%i == 0:
            print(i," ")
            number = number / i
    if number > 2:
        print(number)
except:
    print("Enter only postive integers from 1")