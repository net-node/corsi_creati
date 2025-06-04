class SingleLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = SingleLinkedList('abc')
node2 = SingleLinkedList('def')
node3 = SingleLinkedList('ghi')

node1.next = node2
node2.next = node3

current_node = node1
while current_node:
    print(current_node.data)
    current_node = current_node.next