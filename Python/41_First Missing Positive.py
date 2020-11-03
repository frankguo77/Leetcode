class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positives = set()
        low, up = float('inf'), -float('inf')
        for c in nums:
            if c > 0:
                positives.add(c)
                low = min(low, c)
                up = max(up, c)
                
        if low == float('inf') or low > 1: 
            return 1
       
       
        v = low + 1
        while v <= up:
            if v not in positives:
                return v
            v += 1
        return up + 1
            
        