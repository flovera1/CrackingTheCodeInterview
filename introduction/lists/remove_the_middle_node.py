from singly_linked_list import SingleList
from singly_linked_list import create_singly_list
from singly_linked_list import Node

def length(list):
    size = 0
    current_node = list.head
    while current_node.next is not None:
        size += 1
        current_node = current_node.next
        
    return size


def remove_middle(list):
    node = list.head
    i    = 0
    half = length(list) / 2
    print("half "+str(half))
    while node is not None:
        if half == i:
            value = node.data
            print("value"+str(value))
            list.remove(value)
            break
        i += 1    
        node = node.next



def remove_middel_node(node):
    if (node is None) | (node.next is None):
        return False
    node2       = node.next
    node2.data  = next.data
    node2.next  = node2.next
    
    return True
    
    
    
    
    
    
def main():
    
    s = SingleList()
    s.append(31)
    s.append(2)
    s.append(3)
    s.append(4)
    s.append(3)
 
    s.show()
    remove_middle(s)
    s.show()
        

if __name__ == "__main__":
    main()