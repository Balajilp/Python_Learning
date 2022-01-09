# Try Block in Python
"""
try:
    a = 10 / 0
except Exception as e:
    print(e)

try:
    a = 10 / 2
except Exception as e:
    print(e)
else:
    print("A value: ", a)

try:
    a = 10 / 0
except Exception as e:
    print(e)
else:
    print("A value: ", a)
finally:
    print("Thank You")

# Type  of Exceptions in Python
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))


# Name error exception
try:
    print(a)
except NameError as e:
    print("A is not Defined")

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Denominator cant be Zero")

try:
    name = int("Balaji")
except ValueError as s:
    print("Please Enter Numbers Only")
try:
    list = [10, 20, 30, 40]
    print(list[7])
except IndexError as i:
    print("Invalid Index")

try:
    f = open("For loop.py")
except FileNotFoundError as f:
    print("File Not Found")
else:
    print(f.read())
"""
try:
    a = 10 / 20
    print(a)
    b = [10, 20, 30, 40]
    print(b[6])
except ZeroDivisionError:
    print("denominator cant be zero")
except IndexError:
    print("Invalid Index")