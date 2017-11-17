class mini_stack:
    def __init__(self):
        self.data = [] #store all the data
        self.min  = [] #store the minimum element so far
        
    def push(self, x):
        self.data.append(x)
        
        if len(self.min) == 0 or x <= self.min[-1]:
            self.min.append(x)
            
    def pop(self):
        if len(self.data) == 0:
            return None
        else:
            if self.data[-1] == self.min[-1]: 
                return self.min.pop()
            return self.data.pop()
    def top(self):
        if len(self.data) == 0:
            return None
        else:
            return self.data[-1]
        
    def getMin(self):
        if len(self.minData) == 0:  
            return None         # Empty stack
        else:                       
            return self.minData[-1]
        
    