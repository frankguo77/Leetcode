# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        res = 0
        def helper(node):
            nonlocal res
            if not node:
                return 0
            
            sum_l = helper(node.left)
            sum_r = helper(node.right)
            sum = sum_l + sum_r + node.val
            res += abs(sum_l - sum_r)
            return sum
            
        helper(root)
        return res
        