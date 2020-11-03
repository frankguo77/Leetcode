class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #d[i]: s[0 : i] is OK
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j] and s[j : i] in wordDict:
                    dp[i] = True
                    break
                    
        # print(dp)
                    
        return dp[-1]