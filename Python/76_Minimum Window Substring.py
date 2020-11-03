class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        match = 0 
        l = r = 0
        ans_l , ans_r = -1, len(s)
        while r < len(s):
            if s[r] in counter:
                counter[s[r]] -= 1
                if counter[s[r]] == 0:
                    match += 1
            r += 1
            
            while match == len(counter):
                #print(l,r, ans_l,ans_r)
                if r - l < ans_r - ans_l:
                    ans_l, ans_r = l, r
                if s[l] in counter:
                    counter[s[l]] += 1
                    if counter[s[l]] > 0:
                        match -= 1
                l += 1
            
        return s[ans_l: ans_r] if ans_l != -1 else ""
                    
                
                
                
        
        