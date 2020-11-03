# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(node, p, l):
            if not node:
                return None
            
            dfs(node.left, node, True)
            dfs(node.right, node, False)
            if (not node.left) and (not node.right) and (node.val == target):
                if p:
                    if l == True:
                        p.left = None
                    else:
                        p.right = None
                else:
                    return None
            return node
        
        return dfs(root, None, False)
        
            
        