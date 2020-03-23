# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        pre = None
        ans = True
        def dfs(node):
            nonlocal pre, ans
            if node == None:
                return
            
            if pre is not None and pre != node.val:
                ans = False
                return
            
            pre = node.val
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ans
                
        