# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def can_remove(node):
            if not node:
                return True
            
            l =  can_remove(node.left)
            if l:
                node.left = None
            r = can_remove(node.right)
            if r:
                node.right = None
                
            return l and r and (node.val == 0)
        
        return None if can_remove(root) else root
        

        

        