class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = r = 0
        # [l,r) char
        mem = set() 
        while r < len(s):
            if s[r] in mem:
                res = max(res, len(mem))
                mem.remove(s[l])
                l += 1
            else:
                mem.add(s[r])
                r += 1
 
        res = max(res, len(mem))
        return res

    def lengthOfLongestSubstring2(self, s: str) -> int:
        res = 0
        l = r = 0
        counter = collections.defaultdict(int)
        duplicate = 0

        while r < len(s):
            counter[s[r]] += 1
            if counter[s[r]] > 1:
                duplicate += 1
            r += 1
            
            while duplicate > 0:
                counter[s[l]] -= 1
                if counter[s[l]] > 0:
                    duplicate -= 1
                l += 1
            res = max(res, r - l)         

        return res  

    def lengthOfLongestSubstring3(self, s: str) -> int:
        res = 0
        l = r = 0
        # [l,r) char
        mem = set() 
        while r < len(s):
            while s[r] in mem:
                mem.remove(s[l])
                l += 1
            
            mem.add(s[r])
            r += 1
            res = max(res, r - l)
        return res      