class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    @staticmethod
    def print(current_node: ListNode):
        while current_node:
            print(current_node.data)
            current_node = current_node.next