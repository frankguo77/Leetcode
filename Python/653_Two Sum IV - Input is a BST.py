# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        mem = set()
        def find(node, k):
            if not node: return False
            
            if k - node.val in mem:
                return True
            
            mem.add(node.val)
            return find(node.left, k) or find(node.right, k)
        
        return find(root, k) 

        
        
        
        