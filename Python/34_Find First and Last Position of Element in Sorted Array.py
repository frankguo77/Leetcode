class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]
        
        l, r = 0 , len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
                
        if nums[l] != target:
            return [-1 , -1]
        
        res = [l, l]
        
        r = len(nums) - 1
        while l < r:
            m = l + (r - l + 1) // 2
            if nums[m] <= target:
                l = m
            else:
                r = m - 1
                
        res[1] = r
        
        return res
        
        
        
        
        