### Concept in C++ here

domanda:
in c++ SLL ci servono per creare array di dimensione "dinamica", basta aggiungere un nodo.
Ma in python abbiamo già le liste che sono di memoria dinamica.
Perchè usarle??

Risposta:
While Python’s built-in list covers most needs, singly linked lists are useful when:
1. You need frequent insertions/deletions at the head.
2. You want memory-efficient dynamic growth (no reallocation).
3. You’re implementing stacks, queues, or functional structures.
4. You’re solving linked-list-specific algorithms (e.g., cycle detection).

# 1. You need frequent insertions/deletions at the head.
What Does "Frequent Insertions/Deletions at the Head" Mean?

It refers to adding or removing elements at the beginning of a list very often.

    Insertion at head → Adding a new element as the first item.

    Deletion at head → Removing the first item.

Why Is This Important?

    In a Python list (dynamic array), inserting/deleting at the head is slow (O(n)) because all other elements must be shifted.

    In a singly linked list, inserting/deleting at the head is fast (O(1)) because you just update a pointer.

Example: Python list vs. Linked List
1. Using Python list (Slow for Head Operations)
```python
my_list = [2, 3, 4]

# Insert at head (all elements shift right → O(n))
my_list.insert(0, 1)  # [1, 2, 3, 4]

# Delete at head (all elements shift left → O(n))
my_list.pop(0)  # [2, 3, 4]

```
    Problem: If you do this thousands of times, it becomes inefficient.
2. Using a Linked List (Fast for Head Operations)
```python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):  # O(1)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_at_head(self):  # O(1)
        if self.head:
            self.head = self.head.next

# Usage
ll = LinkedList()
ll.insert_at_head(2)  # 2 → None
ll.insert_at_head(1)  # 1 → 2 → None
ll.delete_at_head()   # 2 → None
```
    Advantage: No shifting! Just pointer updates → Much faster if done repeatedly.
