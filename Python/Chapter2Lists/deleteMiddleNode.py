'''
Implement an algorithm to delete a node in the middle (i.e. any node but the first and last node, 
not necessarily the exact middle) of a singly linked list, given only access to that node.
'''
from linkedList import LinkedList


def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next

ll = LinkedList()
ll.addSeveral([1, 2, 3, 4])
middle_node = ll.add(5)
ll.addSeveral([7, 8, 9])

print(ll)
delete_middle_node(middle_node)
print(ll)
