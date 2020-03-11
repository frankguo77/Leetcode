# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        s = 0
        def helper(node):
            nonlocal s
            if not node:
                return 
            
            helper(node.right)
            node.val = s = node.val + s
            #node.val = s
            helper(node.left)
            
        helper(root)
        return root