'''
Describe how you could use a single array to implement three stacks.
'''

class MultiStack:
	def __init__(self, stacksize):
		self.numbers = 3
		self.array = [0]*(stacksize * self.numstacks)
		self.sizes = [0]*self.numstacks
		self.stacksize = stacksize

	def IsEmpty(self, stacknum):
		return self.sizes[stacknum] == 0

	

	def Push(self, item, stacknum):
		if self.IsFull(stacknum):
			raise Exception("the stack is full")
		self.sizes[stacknum] += 1
		self.array[self.IndexOfTop(stacknum)] = item

	def Pop(self, stacknum):
		if self.IsEmpty(stacknum):
			raise Exception("the stack is empty")
		value = self.array[self.IndexOfTop(stacknum)]
		self.array[self.IndexOfTop(stacknum)] = 0
		self.sizes[stacknum] -= 1
		return value



