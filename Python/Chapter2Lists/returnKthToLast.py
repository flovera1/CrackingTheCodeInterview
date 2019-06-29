'''
Write an algorithm to find the kth to last element of a singly linked list.
'''

'''
Using the 'Runner' method. Maintain two pointers with k-2 nodes
in between. Then slide those two pointer to the right keeping
the distance between them constant. When the right pointer
reaches the end of the list, the left pointer will be pointing
to the kth to the last element.
'''

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self, head):
		self.head = head
		self.tail = head

	def addNode(self, node):
		self.tail.next = node
		self.tail = node

vIp = list(map(int, input().split()))
vK = int(input("kth element"))

vList = LinkedList(Node(vIp[0]))

for i in vIp[1:]:
	vList.addNode(Node(i))

p1=mylist.head
p2=mylist.head
for i in range(k-1):
    p2=p2.next

while p2.next!=None:
    p1=p1.next
    p2=p2.next

print(p1.value)


