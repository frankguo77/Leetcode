# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
#         if not head or not head.next:
#             return head
        
#         j = head
#         cur = head
#         while cur:
#             if cur.val < x:
#                 j.val, cur.val = cur.val, j.val
#                 j = j.next
#             cur = cur.next
#         return head
        p1 = dummy1 = ListNode(0)
        p2 = dummy2 = ListNode(0)
        
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next

        
        p2.next = None
        p1.next = dummy2.next
        
        return dummy1.next
        
        
        
        
                