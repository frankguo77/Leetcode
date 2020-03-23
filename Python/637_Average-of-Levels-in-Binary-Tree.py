# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        
        res = []
        q = collections.deque([(root, 1)])
        while q:
            node, lv = q.popleft()
            if len(res) < lv:
                res.append([0, 0])
            
            res[lv - 1][0] += node.val
            res[lv - 1][1] += 1
            
            if node.left: q.append((node.left, lv + 1))
            if node.right: q.append((node.right, lv + 1))
        
        return [v[0] / v[1] for v in res]
        