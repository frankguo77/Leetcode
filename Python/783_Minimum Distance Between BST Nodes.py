# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        ans = float('inf')
        pre = None
        def dfs(node):
            nonlocal ans, pre
            if not node:
                return 
            
            
            dfs(node.left)
            
            if pre: 
                ans = min(ans, node.val - pre)
            
            pre = node.val
            
            
            dfs(node.right)
            
        dfs(root)
        return ans
            
                
            
            
        