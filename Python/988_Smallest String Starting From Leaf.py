# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        res = 'z' * 13
        def dfs(node, pre):
            nonlocal res
            if not node:
                return pre
            
            pre = chr(97 + node.val) + pre
            if (not node.left) and (not node.right):
                res = min(res, pre)
            
            dfs(node.left, pre)
            dfs(node.right, pre)
            
        dfs(root, "")
        return res
        
        