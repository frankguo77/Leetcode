# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)
        def dfs(node, p, lr):
            if not node: 
                return
            
            if (node.val in to_delete):
                if p:
                    if lr == 0: 
                        p.left = None
                    else: 
                        p.right = None
            elif (not p) or (p.val in to_delete):
                ans.append(node)
            
            #to_delete.remove(node.val)
            dfs(node.left, node, 0)
            dfs(node.right, node, 1)
            
        dfs(root, None, 0)
        return ans
        

            

        
            
        
        
        