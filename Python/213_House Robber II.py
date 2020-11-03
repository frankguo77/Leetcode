class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        def rob_helper(l, r):
            dp1 = dp2 = 0
            for i in reversed(range(l, r + 1)):
                dp1, dp2 = max(nums[i] + dp2, dp1), dp1
            
            return dp1
        
        return max(rob_helper(0, len(nums) - 2), rob_helper(1, len(nums) - 1))
        