# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        left = {}
        res = 0
        def helper(node, lv, pos):
            nonlocal res
            if not node:
                return
            
            left.setdefault(lv, pos)
            res = max(res, pos - left[lv] + 1)
            helper(node.left, lv + 1, 2 * pos)
            helper(node.right, lv + 1, 2 * pos + 1)
            
        helper(root, 0, 0)
        return res

    def widthOfBinaryTree2(self, root: TreeNode) -> int:
        if not root: return 0
        left = []
        res = 0
        q = collections.deque([(root, 0, 0)])
        while q:
            node, lv, pos = q.popleft()
            if len(left) == lv:
                left.append(pos)
            
            res = max(res, pos - left[lv] + 1)
            if node.left:
                q.append((node.left, lv + 1, pos * 2))
            if node.right:
                q.append((node.right, lv + 1, pos * 2 + 1))

        return res
        