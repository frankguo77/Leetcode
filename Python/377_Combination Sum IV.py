class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1) # dp[i]: 选num之前sum为i的总数 
        dp[0] = 1
        for i in range(1, target + 1):
            for c in nums:
                if i >= c:
                    dp[i] = dp[i] + dp[i - c]
                    # print(i, dp[i])
                    
        return dp[-1]
        