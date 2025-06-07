class ListNode:
    def __init__(self, data):
        self.data = data
        self.next : ListNode = None


class LinkedList:
    def __init__(self, head: ListNode):
        self.head : ListNode = head

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def drop_head(self):
        self.head = self.head.next

    def print(self):
        print("(head)", end=" ")
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("NULL")