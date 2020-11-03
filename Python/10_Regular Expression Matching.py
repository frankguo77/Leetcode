import functools
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @functools.lru_cache(maxsize = None)
        def isMatch(i1, i2):
            if i2 == len(p):
                return i1 == len(s)
            
            # if i2 == len(p) or i1 == len(s):
            #     return False
            
            firstmatch = i1 < len(s) and (s[i1] == p[i2] or p[i2] == '.')
            if (i2 < (len(p) - 1)) and p[i2 + 1] == '*':
                return isMatch(i1, i2 + 2) or (firstmatch and isMatch(i1 + 1, i2))
            else:
                return firstmatch and isMatch(i1 + 1, i2 + 1)
            
            
        return isMatch(0, 0)
            
            
            
            
        
        