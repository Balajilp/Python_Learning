# Abstraction and Encapsulation in Python
class Library:
    def __init__(self, books):
        self.books = books

    def list_books(self):
        print("Available Books")
        for book in self.books:
            print(book)

    def borrow_book(self, borrow_book):
        if borrow_book in self.books:
            print("Get your Book Now")
            self.books.remove(borrow_book)
        else:
            print("book not Available")

    def receive_book(self, receive_book):
        print("You have returned the book")
        self.books.append(receive_book)


books = ['c', 'c++', 'Java']
object = Library(books)

msg = """
    1. Display Book
    2. Borrow Book
    3. Return Book
"""
while True:
    print(msg)
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        object.list_books()
    elif ch == 2:
        book = input("Enter the Name to Borrow: ")
        object.borrow_book(book)
    elif ch == 3:
        book = input("Enter Book Name to Return: ")
        object.receive_book(book)
    else:
        print("Thank Hou Come Again")
        quit()
