"""
author - sandeep raj
date - 04/11/2020
time - 21:07
problem statement -"Write a Python program to access and print a URL's content to the console."
"""
from http.client import HTTPConnection
try:
    conn = HTTPConnection("example.com")
    conn.request("GET", "/")
    result = conn.getresponse()
    # retrieves the entire contents.
    contents = result.read()
    print(contents)
except:
    print("EnterValidDomainName")