# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res
        
        q = collections.deque([(root, 1)])

        while q:
            node, lv = q.popleft()
            if len(res) < lv:
                res.append(node.val)
            else:
                if res[lv - 1] < node.val:
                    res[lv - 1] = node.val
            if node.left: q.append((node.left, lv + 1))
            if node.right: q.append((node.right, lv + 1))

        return res        
    
                
                
            
        