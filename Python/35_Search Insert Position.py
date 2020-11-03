class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l + 1) // 2
            # if nums[m] == target:
            #     return m
            if nums[m] <= target:
                l = m  
            else:
                r = m - 1
                
        if nums[l] >= target:
            return l
        
        return l + 1 