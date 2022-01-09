"""
names = {'Balaji', 'Siraj', 'Sudhakar'}
print(names)
print(type(names))
# Access Values Using for loop
for name in names:
    print(name)
# Adding new element
names.add('Sai')
print(names)

# Update another set of data
a = {'Jeeva', 'Deen', 'Sri'}
names.update(a)
print(names)
names.discard("Hi")
print(names)
names.pop()
print(names)
names.clear()
print(names)

del names

names = {'Balaji', 'Siraj', 'Sudhakar', 'Jeeva', 'Balaji', 'Sai', 'Sri', 'Deen'}
print(names)

a = {1, 2, 3, 4}
b = {'a', 'b', 'c', 'd'}
c = a.union(b)
print(c)
a.update(b)
print(a)
c = a.intersection(b)
print(c)
a.intersection_update(b)
print(a)
"""
a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}
"""
c = a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)
"""
c = a.isdisjoint(b)
print(c)
a = {5, 6, 7}
b = {5, 6, 7, 8, 9}
c = a.issubset(b)
print(c)
c = a.issuperset(b)
print(c)