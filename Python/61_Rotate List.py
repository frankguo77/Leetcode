# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
            
        if n <= 1: return head
        
        k = k % n
        if k == 0: return head
        cur = head
        while k > 0:
            cur = cur.next
            k -= 1
        
        # pre = ListNode(0)
        pre = head
        
        while cur.next:
            cur = cur.next
            pre = pre.next
        
        # print(pre.val)
        
        head, cur.next, pre.next = pre.next, head, None
        return head
        