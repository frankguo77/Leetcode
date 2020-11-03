import functools
class Solution:
    def numDecodings(self, s: str) -> int:
        dp2 = 1
        dp1 = 0 if s[0] == '0' else 1
        for i in range(2, len(s)+1):
            dp1, dp2 = (dp1 if 1<=int(s[i-1])<=9 else 0) + (dp2 if 10<=int(s[i-2:i])<=26 else 0), dp1
        return dp1        
        
#         @functools.lru_cache(maxsize = None)
#         def helper(i):
#             if i == len(s):
#                 return 1
            
#             if s[i] == '0':
#                 return 0
            
#             v = helper(i + 1)
#             if (i < len(s) - 1) and (10 <= int(s[i: i + 2]) <= 26):
#                 v += helper(i + 2)
                
#             return v
        
#         if not s:
#             return 0
        
#         return helper(0)
            

            
        
        
        