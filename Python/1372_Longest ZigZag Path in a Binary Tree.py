# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0, 0
            
            ll, lr = dfs(node.left)
            rl, rr = dfs(node.right)
            
            if node.left:
                l = lr + 1
            else:
                l = 0
                
            if node.right:
                r = rl + 1
            else:
                r = 0
                
            res = max(res, l, r)
            return l, r
        dfs(root)
        
        return res

#left: maximum length till this node if the last step is left
#right: maximum length till this node if the last step is right

#Then if we move left, left count of node.left will be 0, right count of node.left will be left + 1; #if we move right, left count of node.right wil be right + 1, right count of node.right will be 0.    
    def longestZigZag2(self, root: TreeNode) -> int:
        q = collections.deque([(root, 0, 0)])
        res = 0
        while q:
            node, l, r = q.popleft()
            res = max(res, l, r)
            if node.left:
                q.append((node.left, 0, l + 1))
            if node.right:
                q.append((node.right, r + 1, 0))
        return res
                        
                
        