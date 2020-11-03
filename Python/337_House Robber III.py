# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        mem = {}
        
        def helper(node):
            if not node:
                return 0
            
            if node in mem:
                return mem[node]
            
            v1 = helper(node.left) + helper(node.right)
            
            v2 = node.val
            if node.left:
                v2 += helper(node.left.left) + helper(node.left.right)
            if node.right:
                v2 += helper(node.right.left) + helper(node.right.right)
            
            res = max(v1, v2)
            mem[node] = res
            return res
        
        return helper(root)
        