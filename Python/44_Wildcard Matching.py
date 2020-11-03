import functools
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @functools.lru_cache(maxsize = None)
        def isMatch(i, j):
            if j == len(p): 
                return ((i == len(s)) or (bool(p) and p[-1] == '*'))
            
            if i == len(s): 
                return j == len(p) or (len(set(p[j:])) == 1 and p[j] == '*')            
            
            if j == len(p):
                return i == len(s)
            
            if p[j] == '*':
                return isMatch(i, j + 1) or isMatch(i + 1, j) or isMatch(i + 1, j + 1)
            else:
                return i < len(s) and p[j] in (s[i], "?") and isMatch(i + 1, j + 1)
                        
        return isMatch(0, 0)
        