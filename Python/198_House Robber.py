class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = dp2 = 0
        for i in reversed(range(len(nums))):
            dp1, dp2 = max(dp2 + nums[i], dp1), dp1
        
        return dp1


            
    
        