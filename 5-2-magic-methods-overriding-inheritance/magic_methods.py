from typing import Any


class Book():
    
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"Book, title: {self.title}, pages: {self.pages}, price: {self.price}"
    
    def __call__(self):
        return f'Now, it is callable object.'


book = Book('Life', 495, 300)
print(book)
print(repr([book, 'qwe', 123]))
print(book())
