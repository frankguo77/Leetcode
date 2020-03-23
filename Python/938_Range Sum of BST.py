# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        s = 0
        def dfs(node):
            nonlocal s, L, R
            if not node:
                return
            
            if L <= node.val <= R:
                s += node.val
            
            if L < node.val:
                dfs(node.left)
            if R > node.val:
                dfs(node.right)
            
        dfs(root)
        return s
        
        