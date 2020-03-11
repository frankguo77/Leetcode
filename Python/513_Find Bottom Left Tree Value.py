# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res = 0
        max_lv = -1
        def helper(node, lv):
            nonlocal res, max_lv
            if not node:
                return
            
            helper(node.left, lv + 1)
            #print(lv, max_val, node.val)
            if lv > max_lv:
                res = node.val
                max_lv = lv
            helper(node.right, lv + 1)

            
            
        helper(root, 0)
        return res

    def findBottomLeftValue2(self, root: TreeNode) -> int:
        res = 0
        max_lv = -1
        q = collections.deque([(root, 0)])
        while q:
            node, lv = q.popleft()
            if lv > max_lv:
                res = node.val
                max_lv = lv
            if node.left:
                q.append((node.left, lv + 1))
            
            if node.right:
                q.append((node.right, lv + 1))
        

        return res
            