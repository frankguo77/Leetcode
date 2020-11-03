class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m + 1] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m
            
        # print(nums[l])
        if not nums or nums[l] != target:
            return -1
        
        return l