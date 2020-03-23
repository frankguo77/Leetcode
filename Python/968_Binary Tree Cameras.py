# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans = 0
        
        
        def dfs(node):
            """
            0 - not cover
            1 - covered
            2 - placed
            """
            nonlocal ans 
            if not node:
                return 1
            
            l = dfs(node.left)
            r = dfs(node.right)
            if l == 0 or r == 0:
                ans += 1
                return 2
            
            if l == 2 or r == 2:
                return 1
            
            return 0
        
        if dfs(root) == 0: ans += 1
        return ans
        