# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.q = collections.deque()
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.q.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v: int) -> int:
        node = self.q[0]
        self.q.append(TreeNode(v))
        if not node.left:
            node.left = self.q[-1]
        else:
            node.right = self.q[-1]
            self.q.popleft()
        return node.val
        

    def get_root(self) -> TreeNode:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()