class Stack:
    def __init__(self):
        self.items = []
        self.min   = []
    def isEmpty(self):
        return self.items == []
    def push (self, item):
        self.items.append(item)
    def push_min(self, item):
        if len(self.min) == 0 or item <= self.min[-1]:
             self.min.append(item)
        self.items.append(item) 
    def min(self):
        if len(self.minData) == 0:  
            return None         # Empty stack
        else:                       
            return self.minData[-1]
    
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def get_min(self):
        if len(self.min) == 0:  
            return None         # Empty stack
        else:                       
            return self.min[-1]
    
    def print_stack(self, stack):
        print(self.min[-1])
        #for i in self.min:
        #    print(i)
    
def main():
    s = Stack()
    s.push_min(2)
    s.push_min(-3)
    s.push_min(0)
    s.push_min(-2)
    s.print_stack(s.get_min())
    
    
if __name__ == "__main__":
    main()