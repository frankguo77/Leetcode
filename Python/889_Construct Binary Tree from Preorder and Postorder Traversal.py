# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def build(i0 , i1, n):
            if n == 0: return None
            root = TreeNode(pre[i0])
            if n == 1:
                return root
            
            # for ln in range(n):
            #     if post[i1 + ln - 1] == pre[i0 + 1]:
            #         break
            
            k = index[pre[i0 + 1]]
            # k = index[pre[i + 1]]      
            ln = k - i1 + 1   
            root.left = build(i0 + 1, i1, ln)
            root.right = build(i0 + ln + 1, i1 + ln, n - ln - 1)
            return root
        
        index = {c : i for i, c in enumerate(post)}

        return build(0, 0, len(pre))
        