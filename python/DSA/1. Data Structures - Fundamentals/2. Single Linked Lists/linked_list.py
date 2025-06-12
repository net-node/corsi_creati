class ListNode:
    def __init__(self, data):
        self.data = data
        self.next : ListNode = None


class LinkedList:
    def __init__(self, data):
        self.head = ListNode(data)
    
    def insert_at_head(self, data):
        old_head = self.head
        self.head = ListNode(data)
        self.head.next = old_head

    def delete_at_head(self):
        if self.head:
            self.head = self.head.next

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def search(self, item):
        last = self.head
        while last.next:
            if last.data == item:
                return last
            last = last.next

    def print(self):
        print("(head)", end=" ")
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("NULL")