"""
   * author - sandeep raj
   * date - 02/11/2020
   * time - 14:48
   * Title -"Write a Python program which accepts the user's first and
last name and print them inreverse order with a space between them."
"""
try:
 firstName = input("enter your First Name : ")
 lastName = input("enter your Last Name : ")
 name = firstName + " " +lastName;
 reversedOrderOfName = name[::-1]

 print (reversedOrderOfName)
except:
  print("enter valid first name and last name");
