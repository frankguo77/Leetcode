# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        prev = -1
        res = float('inf')
        def dfs(root):
            nonlocal res, prev
            
            if root == None:
                return 
            
            dfs(root.left)
            if prev != -1:
                res = min(res, root.val - prev)
            prev = root.val
            dfs(root.right)
            
            
        dfs(root)
        return res