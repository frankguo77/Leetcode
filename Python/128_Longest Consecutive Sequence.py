class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        # print(nums)
        nums.append(float('inf'))
        max_l = 1
        res = 0
        i = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue
            if nums[i + 1] == nums[i] + 1:
                max_l += 1
            else:
                res = max(res, max_l)
                max_l = 1
           
        return res

        def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        s = set(nums)
        max_l = 1
        res = 0
        
        for c in s:
            if c - 1 in s:
                continue
            
            max_l = 1
            t = c + 1
            while t in s:
                max_l += 1
                t = t + 1
                
            res = max(res, max_l)
            
        return res    
        