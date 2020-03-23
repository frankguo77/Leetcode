# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        pre = res = None
        
        def dfs(node):
            nonlocal pre, res
            if node == None:
                return
            dfs(node.left)
            if not pre:
                res = TreeNode(node.val)
                pre = res
            else:
                pre.right = TreeNode(node.val)
                pre = pre.right

            dfs(node.right)
            
        dfs(root)
        return res
       
        