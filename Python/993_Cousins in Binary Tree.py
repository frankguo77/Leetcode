# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        n1 = n2 = None
        def dfs(n, p, d):
            nonlocal n1, n2
            if not n:
                return
            if (not n1) and (n.val == x):
                n1 = n
            elif (not n2) and (n.val == y):
                n2 = n
                
            n.par = p
            n.d = d
            dfs(n.left, n, d + 1)
            dfs(n.right, n, d + 1)
            
        dfs(root, None, 0)
        if (not n1) or (not n2):
            return False
        
        if n1.d != n2.d:
            return False
        
        if n1.par == n2.par:
            return False
        
        # if n1.par.par != n2.par.par:
        #     return False
        
        return True
            
            
            
        