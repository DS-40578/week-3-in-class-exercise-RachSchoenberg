'''
Rachel Schoenberg 
DS 5010
Spring 2025
ICE 3
LinkedList Class

Purpose: Manages the linked list of Book objects and implements operations like counting, filtering, and detecting loops.

Attributes:
head → Points to the first node of the list (default: None)

Methods:
__init__(self): Initializes an empty linked list.
add_to_front(self, data): Adds a book to the front of the list.
__str__(self): Returns a string representation of the entire linked list.
count(self): Calls the recursive count function in Node.
calc_price(self): Calls the recursive price calculation in Node.
to_list(self): Returns a list of all book objects in the linked list.
find_first_index(self, target_value): Finds the first occurrence of a given value.
find_last_index(self, target_value): Finds the last occurrence of a given value.
iterative_filter(self, predicate): Filters books using a lambda function.
has_loop(self): Detects if the list contains a loop using Floyd’s Algorithm.
wrap_around(self, node): Moves a given node to the front and adjusts the list order.

Expected Output:
print(book_list) should display all books in order.
count() should return the correct number of books.
calc_price() should return the total price of paperbacks.
has_loop() should return True if a loop exists, otherwise False.
wrap_around(node) should correctly reposition the list.
'''
from node import Node
from ICEbook import Book

class LinkedList:
    def __init__(self):
        # tart with empty list
        self.head = None

    def add_to_front(self, data):
        # Adds new node to head/front of linkedlist
        # Creates new node w/ data & link to current head
        new_node = Node(data, self.head) 
        # Updates head to new node
        self.head = new_node 

    def __str__(self):
        # Returns str rep of linkedlist
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + " --> "
            current = current.next
        return result + "None"



    def add_to_front(self, data):
        # Adds new node to head/front of linkedlist
        # Creates new node  & links to current head
        new_node = Node(data, self.head)
        # Updates head to new node
        self.head = new_node


    def to_list(self):
        ''' Returns a list of all of the data attributes from each object.'''
        return_list = []
        current = self.head
        while current is not None:
            return_list.append(current.data)
            current = current.next
        return return_list
   

    def find_first_index(self, target_value):
        current = self.head
        index = 0
        while current is not None:
            if current.data == target_value:
                return index
            current = current.next
            index += 1
        # -1 if not found
        return - 1


    def find_last_index(self, target_value):
        '''Returns the index of the last occurance of a target value.'''
        current = self.head
        index = 0
        # initialize as not found/ -1
        last_index = -1
        while current is not None:
            if current.data == target_value:
                last_index = index
            current = current.next
            index += 1
        return last_index
    
    def count(self):
        # If list is emoty, return 0
        return self.head.count() if self.head else 0 
    
    '''
    # If iterating
    def iterative_count(self):
        current = self.head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
        return counter
    '''

    def calc_price(self):
        # Returns total price of all paperback books in linked list
        return self.head.calculate_price() if self.head else 0
    
    def filter(self, predicate):
        '''Filters linked list based on lambda function.

        Param: predicate = lambda that takes in a Node object and returns True/False'
        Returns: New linked list with filtered nodes
        '''
        # new_head = None
        new_ll = LinkedList()
        # New deep copy of just the filtered notes
        current = self.head

        while current is not None:
            if predicate(current):
                #print("Adding", current.data.title, "-->", str(new_head))
                # new_node = Node(current.data, new_head)
                # new_head = new_node
                new_ll.add_to_front(current.data)
            current = current.next
        return new_ll

    def has_loop(self):
        """
        Detects if there is a cycle (loop) in the linked list.
        
        Uses Floyd’s Tortoise and Hare algorithm:
        - A slow pointer moves one step at a time.
        - A fast pointer moves two steps at a time.
        - If they ever meet, a loop exists.
        
        Returns:
            True if there is a loop, otherwise False.
        """
        # CITATION: Floyd's Cycle Finding Algorithm
        # https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/
        # Slow pointer (moves one step)
        slow = self.head  
        # Fast pointer (moves two steps)
        fast = self.head  

        while fast is not None and fast.next is not None:
            # Move slow one step
            slow = slow.next 
            # Move fast two steps 
            fast = fast.next.next  
            
            # If they meet, a loop exists
            if slow == fast:  
                return True
        # No loop found
        return False  

    
    def wrap_around(self, node):
        """
        Moves the given node to the front and wraps the list around it.
        """
        # Does nothing if list = empty or node = invalid
        if self.head is None or node is None:
            return  

        # Find the node before the given node
        prev = None
        tail = self.head
        # Loops through the list until finds node
        while tail.next is not None:
            if tail.next == node:
                prev = tail
            tail = tail.next

        if prev is not None:
            # Disconnect the previous node from the new head
            prev.next = None  

        # Attach the last node to the current head
        tail.next = self.head  
        # Set the new head to the given node
        self.head = node  
        
'''
ll = LinkedList()
ll.add_to_front("A")
ll.add_to_front("C") # Would return 2
ll.add_to_front("B") # Would return 3
ll.add_to_front("A") 
print(ll)
print(ll.find_last_index("A"))
ll.count()

ll.add_to_front(Book("Lake of Souls", False))
ll.add_to_front(Book("Intro to Python", True))
ll.add_to_front(Book("Data Science in Python", False))
ll.add_to_front(Book("Linear Algebra for Dummies", True))
ll.add_to_front(Book("Into The Heart of the Sea", False))
ll.add_to_front(Book("Destroy All Humans", True))

# print(ll.count())
# print(ll.calc_price())
paperback = lambda node: True if node.data.is_paperback else False
new_ll = ll.iterative_filter(paperback)
print(new_ll)
'''