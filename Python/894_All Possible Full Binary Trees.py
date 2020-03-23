import functools
class Solution:
    @functools.lru_cache
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0: return []
        if N == 1: return [TreeNode(0)]
        
        ans = []
        for i in range(1,N,2):
            for l in self.allPossibleFBT(i):
                for r in self.allPossibleFBT(N - i - 1):
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    ans.append(root)
            
        return ans