'''
Rachel Schoenberg
DS 5020
ICE Week 3
Driver File

Purpose:
Initializes a LinkedList containing 10 Book objects.
Tests linked list operations (counting, filtering, indexing, loop detection, wrapping nodes).
Ensures that all assignment requirements are executed correctly.

Attributes:
book_list → LinkedList object storing Book nodes.
books → List of 10 Book objects, containing:
Title (string)
is_paperback (boolean)
Price (9.99 for paperbacks, 19.99 for hardcovers)

Methods:
book_list.add_to_front(book)
Adds each Book object to the front of the linked list.
print(book_list)
Prints the entire linked list, displaying all books in order.
book_list.count()
Prints the total number of books in the list.
book_list.calc_price()
Prints the total price of all paperback books in the list.
book_list.to_list()
Converts and prints the linked list as a Python list.
book_list.find_first_index(target_value)
Finds the first occurrence index of a given book title.
book_list.find_last_index(target_value)
Finds the last occurrence index of a given book title.
book_list.iterative_filter(lambda node: node.data.is_paperback)
Filters and prints only paperback books using a lambda function.
book_list.has_loop()
Checks if the list contains a loop, printing True or False.
book_list.wrap_around(target_node)
Moves a given node to the front and adjusts the list order.
'''
from linked_list import LinkedList
from ICEbook import Book

# Create a LinkedList object
book_list = LinkedList()

# Creating 10 Book objects (some paperback, some hardcover)
books = [
    Book("Animal Farm", True),
    Book("1984", False),
    Book("Dune", True),
    Book("War and Peace", False),
    Book("Don Quixote", True),
    Book("Harry Potter", False),
    Book("The Catcher in the Rye", True),
    Book("The Diary of a Young Girl", False),
    Book("The Odyssey", True),
    Book("The Alchemist", False)
]

# Add books to the linked list
for book in books:
    book_list.add_to_front(book)

# Print the linked list
print("\nLinked List of Books:")
print(book_list)

# Count the number of books in the list
print("\nTotal Number of Books in the List:", book_list.count())

# Calculate total price of paperback books
print("\nTotal Price of Paperback Books: $", round(book_list.calc_price(), 2))
