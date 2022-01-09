class A:
    def display(self):
        print("I am the display of class A")


class B(A):
    def disilay(self):
        print("I am the display of class B")


class C(A):
    def dislay(self):
        print("I am the display of class C")


class D(B, C):
    def display(self):
        print("I am the display of class D")

o = D()
o.display()
