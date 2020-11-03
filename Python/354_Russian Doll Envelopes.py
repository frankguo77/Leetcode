class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n < 2:
            return n
        
        envelopes.sort()
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                        
        return max(dp)


    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n < 2:
            return n
        
        envelopes.sort(key = lambda x:(x[0], -x[1]))
        # print(envelopes)
        res = []
        for _, h in envelopes:
            if not res or res[-1] < h: 
                res.append(h)
            else:
                idx = bisect.bisect_left(res, h)
                if res[idx] > h:
                    res[idx] = h
        return len(res)
            
                    

            
        