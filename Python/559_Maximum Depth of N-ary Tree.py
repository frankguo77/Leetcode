"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
               
        def dfs(node, lv):
            if not node: 
                return lv - 1
            
            if not node.children:
                return lv
            
                      
            return max(dfs(c, lv + 1) for c in node.children)
        
        
        return dfs(root, 1)
                
        
        
        