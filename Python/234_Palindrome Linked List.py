# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(node):
            pre = None
            while node:
                node.next, node, pre,  = pre, node.next, node
            return pre
        
        f = s = head
        while f and f.next:
            f = f.next.next
            s = s.next
        
        if f == None:
            new = reverse(s)
        else:
            new = reverse(s.next)
        
        while new:
            if new.val != head.val:
                return False
            new = new.next
            head = head.next
        
        return True
        
        
                
                
                
        