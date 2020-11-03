class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not (s[l].isalnum()):
                l += 1
                if l == r:
                    return True
            while not (s[r].isalnum()):
                r -= 1
                if l == r:
                    return True
                
            if s[r].lower() != s[l].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
        
        