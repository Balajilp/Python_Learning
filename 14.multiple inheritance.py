# Multiple inheritance

class Father:
    def fishing(self):
        print("fishing in River")

    def chess(self):
        print("Playing Chess From Father")

class Mother:
    def cooking(self):
        print("Cooking Food")

    def chess(self):
        print("Playing Chess From Mother")

class Son(Father, Mother):
    def ride(self):
        print("Rdiging bicycle")


object = Son()
object.ride()
object.fishing()
object.cooking()
object.chess()


