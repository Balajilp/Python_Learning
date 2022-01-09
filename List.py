# List in python
"""
Sequence type
Mutable

a[5]
a = {1,2,3,4,5}
a[0]
"""
a = [1, 2, 3, 4, 5]
print(a)
print(type(a))
a[0] = 100
print(a)
print("Slicing")
print(a[1])
print(a[-1])
print(a[0:3])
print(a[2:])
print(a[:3])

print("------------------------")

a = [1, True, 'Balaji', 2.5, [1, 2, 3, 4]]
print(a)
print(type(a))
print(a[0], "type is", type(a[0]))
print(a[1], "type is", type(a[1]))
print(a[2], "type is", type(a[2]))
print(a[3], "type is", type(a[3]))
print(a[4], "type is", type(a[4]))
print(a[4][1])
print("------------------------")
a = [10, 20, 30, 40]
print(a)
a.clear()
print(a)
a = [10, 20, 30, 40]
b = a.copy()
print(b)
a = [10, 20, 30, 50, 70, 20, 40]
print(a.count(20))
print(a.index(20))
print(len(a))
print(min(a))
print(max(a))
print(a)
a.pop(0)  # Remove Element using indiex
print(a)
a = [10, 20, 30, 50, 70, 20, 40]
a.remove(20)  # Remove Element using values
print(a)
print("------------------------")

names = ['Balaji', "Lakshmi", "Prabha"]
print(names)
name2 = ["Balaji", "Lakshmi"]
names.extend(name2)
print(names)
names.insert(0, "JK")
print(names)
print(list(range(5)))
print(list("Balaji"))
a = [10, 50, 100, 25, 85]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a = ["Apple", "Orange", "Banana","Water Mellon"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
