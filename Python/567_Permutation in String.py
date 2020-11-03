class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1)
        nomatch = len(counter)
        l = r = 0
        while r < len(s2):
            if s2[r] in counter:
                counter[s2[r]] -= 1
                if counter[s2[r]] == 0:
                    nomatch -= 1
            r += 1
            
            if r - l > len(s1):
                if s2[l] in counter:
                    counter[s2[l]] += 1
                    if counter[s2[l]] == 1:
                        nomatch += 1
                l += 1

            if nomatch == 0:
                return True
            
        
        return False
                
                
        