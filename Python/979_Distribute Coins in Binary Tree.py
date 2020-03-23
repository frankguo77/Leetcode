# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if node == None:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            ans += abs(l) + abs(r)
            
            return node.val - 1 + l + r
        dfs(root)
        return ans