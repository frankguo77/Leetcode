class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if not m:
            return 0
        
        n = len(grid[0])
        if not n:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                    
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                    
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        # print(dp)
        return dp[-1][-1]
                    
        
        
        