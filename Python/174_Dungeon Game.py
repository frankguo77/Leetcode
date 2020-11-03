import functools
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        @functools.lru_cache(maxsize = None)
        def helper(i, j):
            if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
                return max(1, 1 - dungeon[-1][-1])
            
            if i == len(dungeon) - 1:
                return max(1, helper(i , j + 1) - dungeon[i][j])
            
            if j == len(dungeon[0]) - 1:
                return max(1, helper(i + 1 , j) - dungeon[i][j])
            
            return max(1, min(helper(i + 1, j), helper(i, j + 1)) - dungeon[i][j])
        
        return helper(0, 0)
                
#         R = len(dungeon)
#         if R == 0: return 0
#         C = len(dungeon[0])
#         if C == 0: return 0
        
#         hp = [[float('inf')] * (C + 1) for _ in range(R + 1)]
#         hp[R][C - 1] = hp[R - 1][C] = 1
        
#         for i in range(R - 1, -1, -1):
#             for j in range(C - 1, -1, -1):
#                 hp[i][j] = max(1, min(hp[i + 1][j], hp[i][j + 1]) - dungeon[i][j])
                
#         return hp[0][0]

        

            
                
            
        