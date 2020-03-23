# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # depth = {None: -1}
        max_d = -1
        def dfs(node, d):
            nonlocal max_d
            if node == None: 
                return
            
            node.d = d
            max_d = max(max_d, d)
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)
        
        dfs(root, 0)
        
        def anser(node):
            nonlocal max_d
            if not node:
                return None
            
            if node.d == max_d:
                return node
            
            l, r = anser(node.left), anser(node.right)
            if l and r:
                return node
            
            return l or r
        
        return anser(root)
                
        
            
            
            
            
        