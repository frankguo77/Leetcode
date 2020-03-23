# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        ans = []
        idx = 0
        def dfs(node):
            nonlocal idx,ans
            if not node:
                return
            
            if node.val != voyage[idx]:
                ans = [-1]
                #print(ans)
                return
            
            idx += 1
            if (node.left) and (node.left.val != voyage[idx]):
                ans.append(node.val)
                node.left, node.right = node.right, node.left
                
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ans
            
        