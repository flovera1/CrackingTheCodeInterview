'''
LIFO
'''

class Node:
	def __init__(self, valData = None, valNext = None, valPrev = None):
		self.data = valData
		self.next = valNext #vaNext is a Node already
		self.prev = valPrev #valPrev is a Node already

class Stack:
	def __init__(self, valHead, valTail, valValues):
		self.head = valHead
		self.tail = valTail
		if not(values is None):
			self.addSeveral(valValues)

	def addSeveral(self, valValues):
		for i in valValues:
			self.add(i)

	def add(self, valValue):
		vNode = Node(valValue)
		if not(self.tail.next is None):
			self.tail.next = vNode
		self.tail = vNode

		if not(valValue.head is None):
			self.head = vNode

	def remove(self):
		vData = self.head.data
		self.head = self.head.next
		if(self.head is None):
			self.tail = None
		return vData
