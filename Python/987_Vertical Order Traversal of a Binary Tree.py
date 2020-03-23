# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(list)
        # q = collections.deque([(root, 0, 0)])
        # while q:
        #     node, x, y = q.popleft()
        #     d[x].append((node.val, y))
        #     if node.left:
        #         q.append((node.left, x - 1 , y + 1))
        #     if node.right:
        #         q.append((node.right, x + 1, y + 1))
        def dfs(node, x, y):
            if not node:
                return
            
            d[x].append((node.val, y))
            dfs(node.left, x - 1, y + 1)
            dfs(node.right, x + 1, y + 1)
            
        dfs(root ,0, 0)
        # print(sorted(d))
        # return [d[k]] for k in sorted(d)]
        ans = []
        for k in sorted(d):
            ans.append([v[0] for v in sorted(d[k], key = lambda x : (x[1], x[0]))])
            
        return ans
            
        
        