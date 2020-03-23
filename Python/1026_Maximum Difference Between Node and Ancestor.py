# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return float('inf'), -float('inf')
            
            if (not node.left) and (not node.right):
                return node.val, node.val

            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)
            min_v, max_v = min(l_min, r_min), max(l_max, r_max)
            
            ans = max(ans, abs(node.val - min_v), abs(max_v - node.val))
            
            return min(l_min, r_min, node.val), max(l_max, r_max, node.val)
        
        dfs(root)
        return ans
            
        