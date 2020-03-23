# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 0, None
            
            l_d, l_lca = dfs(node.left)
            r_d, r_lca = dfs(node.right)
            
            if l_d > r_d:
                return l_d + 1, l_lca
            elif l_d < r_d:
                return r_d + 1, r_lca
            else:
                return l_d + 1, node
            
        return dfs(root)[1]
        