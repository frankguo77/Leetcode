# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import functools

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        #vals = []
        count = collections.defaultdict(int)
        # mem = {}
        
        @functools.lru_cache
        def helper(node):
            if node == None:
                return 0
            
            # if node in mem:
            #     return mem[node]
            
            left = helper(node.left)
            right = helper(node.right)
            val = node.val + left + right
            count[val] += 1
            # mem[node] = val 
            return val
           
        
        helper(root)
        # print(vals)
        if not count: return []
        max_count = max(count.values())
        #print(count.most_common())
        # print(count.items)
        
        return [v for v, c in count.items() if c == max_count]
        
        
        