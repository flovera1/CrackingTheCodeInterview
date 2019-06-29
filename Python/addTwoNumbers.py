# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
    def __str__(self):
        return str(self.val)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        
        vCarry = 0
        vNewList = ListNode(0)
        vTemp = vNewList
        vTotalSum = 0
        while l1 or l2 or vCarry:
            if l1:
                vTotalSum += l1.val
                l1 = l1.next
            if l2:
                vTotalSum += l2.val
                l2 = l2.next
                
            vTotalSum += vCarry
            vCarry = vTotalSum // 10
            vTemp.next = ListNode(vTotalSum % 10)
            vTotalSum = 0
            vTemp = vTemp.next
            
        return vNewList
        

b = Solution()

print(b.addTwoNumbers(ListNode(3), ListNode(9)))