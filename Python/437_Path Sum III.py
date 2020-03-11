# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = 0
        
    def dfs(self,node, num):
        if node == None: 
            return
        if num == node.val: 
            self.res += 1
        self.dfs(node.left, num - node.val)
        self.dfs(node.right, num - node.val)    
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # if self.res == None:
        # self.res = 0
        if root == None: return 0
        self.dfs(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        
        return self.res

    def pathSum2(self, root: TreeNode, sum: int) -> int:
        
        nums = []
        res = 0
        def helper(root):
            nonlocal res
            if root == None:
                return 
            nums.append(root.val)
            addup = 0
            for c in nums[::-1]:
                addup += c
                if addup == sum:
                    res += 1
            helper(root.left)
            helper(root.right)
            
            nums.pop()
        
        helper(root)
        return res

    def pathSum3(self, root: TreeNode, sum: int) -> int:
        pre_sum = collections.defaultdict(int)
        pre_sum[0] = 1
        res = 0

        def helper(root, cur_sum):
            nonlocal res
            if root == None:
                return
            cur_sum += root.val
            
            left = cur_sum - sum
            res += pre_sum[left]
            pre_sum[cur_sum] += 1
            helper(root.left, cur_sum)
            helper(root.right, cur_sum)
            pre_sum[cur_sum] -= 1

        
        helper(root,0)
        return res
                        
                
                
            
        
        