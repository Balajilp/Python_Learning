# IF Statement in python
"""
1. Write a program to check the given number is Even No
2. Write a program tok check vote eligibility by enter his/her name and age
"""
"""
n = int(input("Enter The Number: "))
if n % 2 == 0:
    print(n, "is Even Number")
else:
    print(n, "is Odd Number") 
"""

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
if age >= 18:
    print(name, "age is", age, "Eligible for vote")
else:
    print(name, "age is", age, "Not Eligible for vote")
