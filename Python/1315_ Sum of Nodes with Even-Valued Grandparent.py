# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def dfs(node, p):
            if not node: 
                return
            
            node.p = p
            dfs(node.left, node)
            dfs(node.right, node)
            
        dfs(root, None)
        
        res = 0
        def dfs2(node):
            nonlocal res
            if not node:
                return
            
            #print(node.p)
            if (node.p) and (node.p.p) and (node.p.p.val % 2 == 0):
                res += node.val
                
            dfs2(node.left)
            dfs2(node.right)
                
                
        dfs2(root)
        return res

    def sumEvenGrandparent2(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, p):
            nonlocal res
            if not node: 
                return
            
            node.p = p
            if (node.p) and (node.p.p) and (node.p.p.val % 2 == 0):
                res += node.val
            dfs(node.left, node)
            dfs(node.right, node)
            
        dfs(root, None)
        
        return res
        
        