# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root: 
            return -1
        min_v = root.val
        res = float('inf')
        def dfs(node):
            nonlocal min_v, res
            if not node:
                return -1
            if res > node.val > min_v:
                res = node.val
            elif node.val == min_v:
                dfs(node.left)
                dfs(node.right)

                
        dfs(root)
        
        return res if res != float('inf') else -1
        