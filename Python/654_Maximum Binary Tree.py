# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
#         def findmaxids(nums):
#             max_v = None
#             max_idx = -1
#             for i, c in enumerate(nums):
#                 if max_v == None or c > max_v:
#                     max_idx = i
#                     max_v = c
#             return max_idx
        
#         if not nums:
#             return None
        
#         cut = findmaxids(nums)
#         root = TreeNode(nums[cut])
#         root.left = self.constructMaximumBinaryTree(nums[:cut])
#         root.right = self.constructMaximumBinaryTree(nums[cut + 1: ])
#         return root
         if not nums: return None
         root = TreeNode(max(nums))
         root.left, root.right = self.constructMaximumBinaryTree(nums[:nums.index(max(nums))]),                                        self.constructMaximumBinaryTree(nums[nums.index(max(nums))+1:])
         return root
        
        
                
        