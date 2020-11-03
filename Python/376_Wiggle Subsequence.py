class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        #u : [0, i] max num of final up ending with nums[i]
        #d:  [0, i] max num of final down ending with nums[i]
        if not nums:
            return 0
        u = d = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                u = d + 1
            elif nums[i] < nums[i - 1]:
                d = u + 1
                
        return max(u, d)

    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        preD = nums[1] - nums[0]
        ans = 1 + (preD != 0)
        
        for i in range(2, len(nums)):
            d = nums[i] - nums[i - 1]
            if preD * d < 0 or (d != 0 and preD == 0):
                ans += 1
                preD = d
        
        return ans

        

           
            
        