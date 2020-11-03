class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = r = 0
        res = len(nums) + 1
        
        while r < len(nums):
            s -= nums[r]
            r += 1
            
            while s <= 0:
                res = min(res, r - l)
                if res == 1:
                    return res
                
                s += nums[l]
                l += 1
                
        return 0 if res > len(nums) else res

    