# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        pre = dummy = TreeNode(-1)
        pre.left = pre.right = root
        
        def helper(p, c, lv, left):
            if lv == d:
                if left or c == root:
                    p.left = TreeNode(v)
                    p.left.left = c
                else:
                    p.right = TreeNode(v)
                    p.right.right = c
                
                return
            if c == None: return
            
            helper(c, c.left, lv + 1, True)
            helper(c, c.right, lv + 1, False)
            
        helper(pre, root, 1, True)
        return dummy.left

    def addOneRow2(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        def helper(node, lv):
            if node == None: 
                return
            if lv == d - 1:
                l, r = node.left, node.right
                new = TreeNode(v)
                node.left = new
                node.left.left = l
                
                new = TreeNode(v)
                node.right = new
                node.right.right = r
                return
            
            
            helper(node.left, lv + 1)
            helper(node.right, lv + 1)
            
        if d == 1:
            new = TreeNode(v)
            new.left = root
            return new 
        else:
            helper(root, 1)
            return root

    def addOneRow3(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new = TreeNode(v)
            new.left = root
            return new
        q = collections.deque([(root, 1)])
        while q:
            node,lv = q.popleft()
            if lv == d - 1:
                l, r = node.left, node.right
                new = TreeNode(v)
                node.left = new
                new.left = l

                new = TreeNode(v)
                node.right = new
                new.right = r
            else:
                if node.left: q.append((node.left, lv + 1))
                if node.right: q.append((node.right, lv + 1))
                    
        return root            
                
        
                
            
                    
            
        

                

                