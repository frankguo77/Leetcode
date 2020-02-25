# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.len = 0
        while head:
            self.len += 1
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        
        i = random.randint(0, self.len - 1)

        node = self.head
        while i > 0:
            node = node.next
            i -= 1
            
            
        return node.val
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()