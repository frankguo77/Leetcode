class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for c in nums:
                if c in path:
                    continue
                    
                path.append(c)
                helper(path)
                path.pop()
                
        helper([])
        return res