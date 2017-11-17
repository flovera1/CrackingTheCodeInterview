from singly_linked_list import SingleList
from singly_linked_list import create_singly_list

def kth_to_last(list, k):
    node      = list.head
    container = []
    j         = 0    
    while node is not None:
        if j >= k:
            container.append(node.data)                    
        j += 1
        node = node.next
        
    return container

def main():
    s  = SingleList()
    r0 = SingleList()
    r  = SingleList() 
    s.append(31)
    s.append(2)
    s.append(3)
    s.append(31) 
    s.append(6) 
    s.show()
    temp = kth_to_last(s, 2)
    #temp = remove_without_buffer(s)
    r0   = create_singly_list(temp)
    print("from kth element k == 2")
    r0.show()
    
if __name__ == "__main__":
    main()
