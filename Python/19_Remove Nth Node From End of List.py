# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = dumy = ListNode(0)
        dumy.next = head
        while n > 0:
            #head = head.next
            head = head.next
            n -= 1
            
        while head:
            pre = pre.next
            head = head.next
            
        pre.next = pre.next.next
        
        return dumy.next
            
            
        
        
        