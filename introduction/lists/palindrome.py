from doubly_linked_list import Node
from doubly_linked_list import DoubleList

def is_palindrome(l):
    head = l.head
    prev = None
    
    while head.next is not None:
        l.prev = prev
        prev   = head
        l      = head.next
        head   = head.next
        
        
    tail      = l
    tail.prev = prev
    while head is not tail and head.data == tail.data:
        head = head.next
        tail = tail.prev
    if head is tail:
        return True
    elif head.data == tail.data:
        return True
    else:
        return False
    
    
    
def main():
    n1      =   Node(1, None, None)
    n2      =   Node(2, None, None)
    n3      =   Node(1, None, None)
    n4      =   Node(3, None, None)
    l = DoubleList()
    l.append(n1)
    l.append(n2)
    l.append(n3)
    l.append(n4)
    print(is_palindrome(l))
   
    
    
if __name__ == "__main__":
    main()
    