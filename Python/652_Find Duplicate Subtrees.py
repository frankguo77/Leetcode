# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []
        def helper(node):
            if not node:
                return None
            uid = trees[node.val, helper(node.left), helper(node.right)]
            count[uid] += 1
            if count[uid] == 2:
                ans.append(node)
            return uid
        
        helper(root)
        return ans

    def findDuplicateSubtrees2(self, root: TreeNode) -> List[TreeNode]:
        # trees = collections.defaultdict()
        # trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []
        def helper(node):
            if not node:
                return '#'
            # uid = trees[node.val, helper(node.left), helper(node.right)]
            uid = f'{node.val}{helper(node.left)}{helper(node.right)}'
            count[uid] += 1
            if count[uid] == 2:
                ans.append(node)
            return uid
        
        helper(root)
        return ans
                