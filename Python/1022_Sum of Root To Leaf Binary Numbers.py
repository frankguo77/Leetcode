# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, res):
            nonlocal ans
            
            if not node:
                return
            
            res = (res << 1) + node.val
            #res += node.val
            #print(res)
            if (not node.left) and (not node.right):
                ans += res
                
                
            dfs(node.left, res)
            dfs(node.right, res)
            
        dfs(root, 0)
        return ans
                
                
            
        