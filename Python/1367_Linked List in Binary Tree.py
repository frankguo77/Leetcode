# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(l_node, t_node):
            if not l_node:
                return True
            
            if not t_node:
                return False
            
            if t_node.val == l_node.val:
                return dfs(l_node.next, t_node.left) or dfs(l_node.next, t_node.right)
            else:
                return False

                
        if not head: return True
        if not root: return False
        
        if head.val == root.val:
            if dfs(head, root):
                return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
                
        
        