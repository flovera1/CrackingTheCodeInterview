'''
Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting
'''

from linkedList import LinkedList

def intersection(valList1, valList2):
	shorter = valList2 if(len(valList1) > len(valList2)) else valList2
	larger  = valList2 if(len(valList2) > len(valList1)) else valList1
	print(shorter)
	print(larger)
	
	for i in shorter:
		for j in larger:
			if i.value == j.value:
				return i.value


_vl1 = LinkedList()
_vl2 = LinkedList()

_vl1.addSeveral([1, 2, 3, 4])
_vl2.addSeveral([0, 0, 0, 2])

print(intersection(_vl1, _vl2))
