class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m,n = len(haystack), len(needle)
        if n == 0: return 0
        if m == 0:return -1
        
        
        for i in range((m - n + 1)): # should plus 1???
            #print(haystack[i:i+n])
            if haystack[i:i+n] == needle:
                return i

            
        return -1
                
            
            
            
    
        