from single_linked_list import ListNode, SingleLinkedList

head = ListNode('a')
alphabet = "bcdefghijklmnopqrstuvwxyz"

def build_linked_list():
    for char in alphabet:
        head.next = ListNode(char)
        head = head.next

print(head.data)

