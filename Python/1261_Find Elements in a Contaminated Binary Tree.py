# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.s = set()
        def dfs(node, v):
            if not node:
                return
            # if v == 0:
            node.val = v
            self.s.add(v)
            # if node.left:
            #     # node.left.val = 2*node.val + 1
            dfs(node.left, 2*node.val + 1)
            # if node.right:
            dfs(node.right, 2*node.val + 2)
                
        dfs(root, 0)
        # self.root = root
        

    def find(self, target: int) -> bool:
        return target in self.s
#         def dfs(root):
#             if not root:
#                 return False
            
#             if root.val == target:
#                 return True
#             elif root.val < target:
#                 return dfs(root.right) or dfs(root.left)
#             else:
#                 return False
#         return dfs(self.root)

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)