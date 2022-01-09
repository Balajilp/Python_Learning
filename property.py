class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.msg = self.name + " is " + str(self.age) + " year old"

    @property
    def msg(self):
        return self.name + " is " + str(self.age) + " year old"

o = user("Balaji", 20)
print(o.name)
print(o.age)
print(o.msg)
o.age = 45
print(o.msg)