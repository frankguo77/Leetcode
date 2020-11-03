class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        l = r = 0
        left = maxCost
        while r < len(s):
            cost = abs(ord(s[r]) - ord(t[r]))
            left -= cost
            r += 1 
            
            while left < 0:
                cost = abs(ord(s[l]) - ord(t[l]))
                #print(l,cost,left)
                left += cost
                #print(left)
                if left > maxCost:
                    left = maxCost
                l += 1
                #print(l, left)
            
            res = max(res, r - l)
        
        return res
                
                
                
        