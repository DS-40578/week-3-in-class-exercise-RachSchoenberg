'''
Rachel Schoenberg 
DS 5010
Spring 2025
ICE 3
Node Class

Purpose: Represents a single node in a linked list, storing a Book object and a reference to the next node.

Attributes:
data → Stores a Book object
next → Pointer to the next Node (default: None)

Methods:
__init__(self, data, next_node=None): Initializes node with a book and a reference to the next node.
__str__(self): Returns a string representation of the book stored in the node.
count(self): Recursively counts the number of nodes in the list.
calculate_price_paperback(self): Recursively calculates the total price of all paperback books in the list.

Expected Output:
If count() is called on a linked list of 5 nodes, it should return 5.
If calculate_price_paperback() is called, it should return the total price of all paperback books.

'''
class Node:
    # Represents a single node in a linked list.
    # Each node stores data & reference to next node.

    def __init__(self, data, next_node = None):
        # Stores that data
        self.data = data 
        # Points to next node in linkedlist
        self.next = next_node

    def __str__(self):
        # Returns string rep of node's data
        return str(self.data)
    
    def count(self):
        # Recursively counts # of nodes
        print("In the Node that stores", self.data)
        # Base Case
        if self.next is None:
            print("Hit our base case! Returning 1\n")
            return 1 
        # Recursive Case
        else:
            print("Recursive call! Calling count with the node storing", self.next)
            return 1 + self.next.count()
        
    def calculate_price(self):
        # Recursively calculates price of all books
        if self is None:
            return 0
        # Base Case
        current_price = self.data.price if self.data.is_paperback else 0
        # Recursive Case
        return current_price + (self.next.calculate_price() if self.next else 0)