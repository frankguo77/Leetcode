# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        res = [None]
        def dfs(root):
            if not root:
                return
            
            if root.val == target.val:
                res[0] = root
                return
            
            dfs(root.left)
            dfs(root.right)
        dfs(cloned)
        return res[0]

    def getTargetCopy2(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
       def isEqual(n1, n2):
            if n1 is n2:
                return True
            
            if (not n1) or (not n2):
                return False
            
            if n1.val != n2.val: return False
            return isEqual(n1.left, n2.left) and isEqual(n1.right, n2.right)
        
        q = collections.deque([cloned])
        while q:
            n = q.popleft()
            if n.val == target.val:
            # if isEqual(target, n):
                return n
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        return None
        
        