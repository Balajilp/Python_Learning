class user:
    course = "python"


o = user()
print(user.__dict__)
print(user.course)  # Print class attribute
print(o.__dict__)
print(o.course)
o.course = "Java"
print(o.__dict__)
print(o.course)

o2 = user()
print(o2.course)

