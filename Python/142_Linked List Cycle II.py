# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:           
        
#         if head is None or head.next is None:
#                 return None
        
        
#         s = head.next
#         f = head.next.next
        
#         while s != f:
#             if s is None or f is None or f.next is None:
#                 return None
#             s = s.next
#             f = f.next.next
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                break
        else:
            return None
        
        s = head
        while s!= f:
            s = s.next
            f = f.next
        return s
        