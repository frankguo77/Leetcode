# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getMaxDepth(node):
            if not node: return 0
            
            return max(getMaxDepth(node.left), getMaxDepth(node.right)) + 1
        
        max_d = getMaxDepth(root)
        n = 2**max_d - 1
        res = [[''] * n for _ in range(max_d)]
        
        def fill(node, l, r, lv):
            if not node: return
            mid = (r + l) // 2
            res[lv][mid] = str(node.val)
            fill(node.left, l, mid - 1, lv + 1)
            fill(node.right, mid + 1, r, lv + 1)
        
        fill(root, 0, n - 1, 0)
        return res
            
            
            
        
        # q = collections.deque([(root, 0)])
        # while q:
        #     node, lv = q.popleft()
        #     if len(res) == lv:
        #         res.append([""] * n)
        #     res[lv]
        