from singly_linked_list import SingleList
from singly_linked_list import create_singly_list
from singly_linked_list import Node

def partition (list, key):
    current_node = list.head
    pre = SingleList()
    post = SingleList()
    while current_node is not None:
        if current_node.data != key:
            if current_node.data > key:
                 post.append(current_node.data)
            else:
                pre.append(current_node.data)
        current_node = current_node.next
    current_node = pre.head
    new_node = Node(key, post.head)
    while current_node.next is not None:
        current_node = current_node.next
    current_node.next = new_node
    return pre

def main():
    s = SingleList()
    s.append(6)
    s.append(3)
    s.append(8)
    s.append(1)
    s.append(5)
    s.append(9)
    s.show()
    
    p = partition(s, 5)
    p.show()
    
    
if __name__ == "__main__":
    main()