class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.defaultdict(int)
        l = r = 0
        res = 0
        while r < len(s):
            counter[s[r]] += 1
            r += 1
            
            while r - l - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            
            res = max(res, r - l)
        return res
            
        