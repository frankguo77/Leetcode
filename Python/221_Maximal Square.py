import functools
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        @functools.lru_cache(maxsize = None)
        def helper(i, j):
            nonlocal maxl
            if i == 0 or j == 0:
                return int(matrix[i][j])
           
            
            if int(matrix[i][j]) == 1:
                res = min(helper(i - 1, j - 1), helper(i - 1, j), helper(i, j - 1)) + 1
            else:
                res = 0
  
            return res

        M = len(matrix)
        if not M:
            return 0
        
        N = len(matrix[0])
        if not N:
            return 0
        
        maxl = 0
        for i in range(M):
            for j in range(N):
                if int(matrix[i][j]) == 1:
                    maxl = max(maxl, helper(i, j))
       
        return maxl ** 2
                
            
            
#         R = len(matrix)
#         if R == 0: return 0
#         C = len(matrix[0])
#         if C == 0: return 0
        
#         dp = [[0] * C for _ in range(R)]
#         l = 0
#         for i in range(R):
#             for j in range(C):
#                 dp[i][j] = int(matrix[i][j])
#                 if i and j and dp[i][j]:
#                     dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
#                 l = max(l, dp[i][j])
#         #print(dp)
#         return l**2
        
        
        