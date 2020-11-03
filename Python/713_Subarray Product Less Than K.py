class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        if k <= 0: return 0
        res = 0
        l = r = 0
        product = 1
        while r < len(nums):
            product *= nums[r]
            r += 1
            
            while l < r and product >= k:
                product //= nums[l]
                l += 1
                
            res += (r - l)
                
        return res
            
        