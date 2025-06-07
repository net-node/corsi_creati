from linked_list import ListNode, LinkedList

head = ListNode('a')
ll = LinkedList(head)

def build_linked_list(ll: LinkedList):
    for char in "bcdefgh":
        ll.append(char)

build_linked_list(ll)
ll.print()

new_head = ListNode("0")
new_head.next = ll.head
ll.head = new_head
ll.print()

ll.head = ll.head.next.next.next
ll.print()