"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root: 
            return res
        
        q = collections.deque([(root, 0)])
        while q:
            node, lv = q.popleft()
            if len(res) == lv:
                res.append([])
            
            res[lv].append(node.val)
            
            for n in node.children:
                if n: q.append((n, lv + 1))
                    
        return res
            
        