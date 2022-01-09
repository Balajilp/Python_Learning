# Static method in python
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetail(self):
        print("Name: ", self.name, "Age : ", self.age)

    @staticmethod
    def welcome():
        print("Welcome to our Institution")

object = student("Siraj", 22)
object.printDetail()
object.welcome()

object2 = student("sudhakar", 20)
object2.printDetail()