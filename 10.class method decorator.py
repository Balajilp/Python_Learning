class student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.count += 1

    def printall(self):
        print("Name : ", self.name, " Age : ", self.age)

    @classmethod
    def total(cls):
        return cls.count


object = student("Lakshmi Prabha", 18)
object.printall()
print("Total Admission: ", object.total())

object2 = student("Balaji", 20)
object2.printall()
print("Total Admission: ", student.total())
print("Total Admission: ", object.total())
