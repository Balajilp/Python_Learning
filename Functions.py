def welcome():
    print("Welcome to Balaji Home")


welcome()

# No Return type Without Argument Function in python
"""
def add():
    a = int(input("Enter the Value of A: "))
    b = int(input("Enter the Value of B: "))
    c = a + b
    print("Total", c)
add()
"""
# No Returns With Arugument Function in Python
"""
def sub(a, b):
    c = a - b
    print("Difference : ", c)
sub(20, 18)
"""
# Return Type Without Argument Function in python

"""
def mul():
    a = int(input("Enter the Value of A: "))
    b = int(input("Enter the Value of B: "))
    c = a * b
    return c
x = mul()
print("Mul ",x)
"""
# Return Type With Argument Function in Python
"""
def div(a, b):
    c = a / b
    return c

x = div(20, 2)
print("Division", x)
"""
# Arbitrary Arguments Function in Python
"""
def class_10(*students):
    print(students)
    for user in students:
        print(user)

class_10("Balaji", "siraj", "Sudahkar", "Sai", "sri", "Deen")
"""
# Keyword Argument Function in Python
"""
def message(name, age):
    print(name, " age is ", age)


message(age=20, name="Balaji")
"""
# Arbitrary Keyword Arguments in Python
"""
def bioData(**data):
    print(data)

bioData(name="Balaji", age=20, gender="male")
"""
# Default Parameter Function in python
"""
def user(name,city="Trichy"):
    print(name," is from", city)

user("Balaji", "Thuraiyur")
user("Gokul")
"""
# Passing List as an Argument in Function Python
"""
def total(marks):
    return sum(marks)
print("Total: ", total([55,75,80,95,47]))
"""
# recursive function
# 1* 2* 3* 4* 5 = 120
"""
def factorial(x):
    if x==1:
        return 1
    else:
        return (x * factorial(x - 1))

print("Factorial : ", factorial(5))
"""
"""
factorail(5)
5 * factorial(4)
5 * 4 * factortial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 *  1 
"""
# Lambda Function in Python
c = lambda a: a + 50
print(c(5))

c = lambda a,b: a * b
print(c(10, 25))
