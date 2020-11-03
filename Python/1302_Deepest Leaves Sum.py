# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res, max_d = 0,-1
        def dfs(node, d):
            nonlocal res, max_d
            if not node:
                return
            
            if d == max_d:
                res += node.val
            elif d > max_d:
                res = node.val
                max_d = d
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)
            
        dfs(root, 0)
        return res
            
        