import functools
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        @functools.lru_cache(maxsize = None)
        def helper(i1, i2, i3):
            if i1 + i2 != i3:
                return False
            
            if i1 == 0 and i2 == 0 and i3 == 0:
                return True
            
            if (i1 > 0 and s1[i1 - 1] == s3[i3 - 1] and helper(i1 - 1, i2, i3 - 1)) or \
               (i2 > 0 and s2[i2 - 1] == s3[i3 - 1] and helper(i1, i2-1, i3-1)):
                    return True
                
            return False
        
        return helper(len(s1), len(s2), len(s3))
        