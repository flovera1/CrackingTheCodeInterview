'''
Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only
need to be after the elments less than x (see below). The partition element x can appear anywhere
in the "right partition". It does not need to appear between the left and right partitions.
'''

from linkedList import LinkedList
from linkedList import Node

def createPartition(valLinkedList, partition):
	vFirstPartition = LinkedList()
	vNode = valLinkedList.head
	vSecondPartition = LinkedList()

	while(vNode != None):
		if (vNode.value < partition):
			#add the node to the vFirstPartition
			vFirstPartition.add(vNode)

		elif(vNode.value > partition):
			#print(vNode)
			vSecondPartition.add(vNode)

		elif(vNode.value == partition and vNode.next == None):
			vSecondPartition.add(Node)

		vNode = vNode.next


	#print(vFirstPartition)
	#print(vSecondPartition)	
	return vFirstPartition.mergeLists(vSecondPartition)
	

ll = LinkedList()
ll.addSeveral([3,5,8,5,10,2])
#print(ll)
print(createPartition(ll, 5))
#print("-------------")
#print(ll)


