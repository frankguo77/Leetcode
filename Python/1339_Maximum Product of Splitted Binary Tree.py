# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        n2s = {}
        def dfs(node):
            if not node:
                return 0
            
            l, r = dfs(node.left), dfs(node.right)
            #print(l, r)
            n2s[node] = l + r + node.val
            return l + r + node.val
        dfs(root)
        
        return max((n2s[root] - n2s[i]) * n2s[i] for i in n2s) % (10**9 + 7)
             