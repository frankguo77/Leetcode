# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        #if not preorder: return None
        
        def helper(l, r):
            if l > r:
                return None
            
            root = TreeNode(preorder[l])
            r_start = l + 1
            while r_start <= r:
                if preorder[r_start] > preorder[l]:
                    break
                r_start += 1
            
            root.left = helper(l + 1, r_start - 1)
            root.right = helper(r_start, r)
            return root
        
        return helper(0, len(preorder) - 1)
        
        
            
                
        