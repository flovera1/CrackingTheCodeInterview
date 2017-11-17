from singly_linked_list import SingleList
from singly_linked_list import create_singly_list
from singly_linked_list import Node

def sum(list1, list2):
    v1 = list1.head 
    v2 = list2.head
    carry = 0
    while v1 is not None:
        val     = ((v1.val + v2.val) % 10) + carry
        carry   = (v1.val + v2.val) // 10
        v1.val  = val
        v1      = v1.next
        v2      = v2.next
        
    cur = list1.head
    val = 0
    mul = 1
    while cur is not None:
        val = val + (cur.val * mul)
        mul = mul * 10
        cur = cur.next

    return val
        