class Student():
    name = "Balaji"
    age = 20


# getattr(get attribute) methode
print(getattr(Student, "name"))
print(getattr(Student, "age"))
print(getattr(Student, "gender", "No Such Attribute Found"))

# Dot Notation
print(Student.name)
print(Student.age)

# setattr method
setattr(Student, 'name', 'Lakshmi Prabha')
print(Student.name)

setattr(Student, 'gender', 'Female')
print(Student.gender)

Student.city = "Thuraiyur"
print(Student.city)
print(Student.__dict__)
delattr(Student, "gender")
print(Student.__dict__)
del Student.age
print(Student.__dict__)
