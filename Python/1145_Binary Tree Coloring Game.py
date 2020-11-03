# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        l = r = 0
        def dfs(node):
            nonlocal l, r
            if not node:
                return 0
            l_c, r_c = dfs(node.left), dfs(node.right)
            if node.val == x:
                l,r = l_c, r_c
            
            return l_c + r_c + 1
        dfs(root)
        return max(l, r, n - l - r - 1) > n // 2
        