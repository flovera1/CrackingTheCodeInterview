from random import randint

class Node:
    def __init__(self, valNode, valNextNode= None, valPrevNode=None):
        self.value = valNode
        self.next = valNextNode
        self.prev = valPrevNode

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.addSeveral(values)

    def __iter__(self):
        vHead = self.head
        while (vHead):
            yield(vHead)
            vHead = vHead.next

    def __str__(self):
        vValues = [str(x) for x in self]
        return '->'.join(vValues)

    def __len__(self):
        counter = 0
        node = self.head
        while(node.next):
            counter += 1
            node = node.next

        return counter


    def mergeLists(self,valL):
        #print(self.tail.next)
        #print(valL1.head.next)
        self.tail.next = valL.head
        self.__str__()
        vNewFormedList = LinkedList()
        vNodeHead = self.head
        vNodeHeadvalL = valL.head
        while(vNodeHead.next):

            vNewFormedList.add(vNodeHead)
            vNodeHead = vNodeHead.next

        while(vNodeHeadvalL.next):
            vNewFormedList.add(vNodeHeadvalL)
            vNodeHeadvalL = vNodeHeadvalL.next

        vNewFormedList.__str__()
        print(vNewFormedList)
        return vNewFormedList
            

    def add(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def addSeveral(self, valValues):
        for i in valValues:
            self.add(i)

    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


