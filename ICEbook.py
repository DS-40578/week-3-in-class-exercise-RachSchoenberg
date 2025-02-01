'''
Rachel Schoenberg 
DS 5010
Spring 2025
ICE 3
Book Class

Purpose: Represents a book with attributes for title, paperback status, and price.

Attributes:
title → String (Title of the book)
is_paperback → Boolean (True if paperback, False if hardcover)
price → Float (Automatically set to $9.99 for paperbacks, $19.99 for hardcovers)

Methods:
__init__(self, title, is_paperback): Initializes book attributes.
__str__(self): Returns a formatted string representation of the book.

Expected Output:
When creating a Book("Dune", True), print(book) should output:
"Dune" (Paperback: True) - $9.99
'''

class Book:
    def __init__(self, title, is_paperback):
        # Book title
        self.title = title 
        # True = paperback, False = hardcover
        self.is_paperback = is_paperback 

        # Price based on paperback or hardcover
        if is_paperback:
            self.price = 9.99
        else:
            self.price = 19.99

    def __str__(self):
        # Returns a string representation of the book.
        return f'"{self.title}" (Paperback: {self.is_paperback}) - ${self.price:.2f}'