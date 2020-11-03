# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def dfs(node, l):
            if not node:
                return l
            
            dfs(node.left, l)
            l.append(node.val)
            dfs(node.right, l)
            return l
        l1, l2 = dfs(root1,[]), dfs(root2,[])
        
        i = j = 0
        res = []
        while (i < len(l1)) and (j < len(l2)):
            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        
        while i < len(l1):
            res.append(l1[i])
            i += 1
        while j < len(l2):
            res.append(l2[j])
            j += 1

        
        return res
            
        