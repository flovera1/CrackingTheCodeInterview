from lib2to3.fixer_util import Number
from test import test_bool
class one_array_three_stacks:
    def __init__(self, stackSize):
        self.stackCapacity  = stackSize
        self.numberOfStacks = 3
        self.values         = []
        self.sizes          = [0,0,0]
        
    def push (self, stackNum, value):
        self.values.append(value)
        if stackNum == 0:
            self.sizes[0] += 1
        elif stackNum == 1:
            self.sizes[1] += 1
        else: # stackNum == 2
            self.sizes[2] += 1
        
    def pop (self, stackNum):
        topIndex = indexOfTop(stackNum)
        value    = self.values[topIndex]
        self.values[topIndex] = 0
        if stackNum == 0:
            self.sizes[0] -= 1
        elif stackNum == 1:
            self.sizes[1] -= 1
        else:
            self.sizes[2] -= 1
        
        return value
        
    #return the top element
    def peek (self, stackNum):
        return self.values[indexOfTop(stackNum)]
    
    def isEmpty(self, stackNum):
        bool = False 
        
        if self.sizes[0] == 0 & self.sizes[1] == 0 & self.sizes[2] == 0:
            bool = True
        return bool
        
        
    def isFull(self, stackNum):
        return self.sizes[stackNum] == self.stackCapacity
        
    # returns index of the top of the stack
    def indexOfTop(self, stackNum):
        offset = stackNum * self.stackCapacity
        size   = self.sizes[stackNum]
        
        return offset + size - 1