from singly_linked_list import SingleList
from singly_linked_list import create_singly_list

from doubly_linked_list import DoubleList


def sinlgy_remove_duplicates (list):
    current_node    = list.head
    elements        = []
    while current_node is not None:
        if current_node.data in elements:
            current_node = current_node.next
        else:
            elements.append(current_node.data)
            current_node = current_node.next
    return elements # you have a list of elements

            
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


    temp = sinlgy_remove_duplicates(s)
    #temp = remove_without_buffer(s)
    r0   = create_singly_list(temp) 

    print("after removing duplicates:")
    r0.show()

if __name__ == "__main__": 
    main()