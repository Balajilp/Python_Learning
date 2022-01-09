# init method in python
class user:
    def __init__(self,name):
        print("Call When New Instance Created")
        self.name=name
    def printall(self):
        print("Name: ", self.name)


o1 = user("Balaji")
o1.printall()
print(o1.__dict__)
o2 = user("Lakshmi prabha")
o2.printall()
print(o2.__dict__)
print(user.__dict__)



