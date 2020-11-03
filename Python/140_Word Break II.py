import functools
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
      
        wordDict = set(wordDict)
        
        @functools.lru_cache
        def bt(word):
            res = []
            if word in wordDict:
                res.append(word)
                
            for j in range(1, len(word) + 1):
                w1 = word[0 : j]
                if w1 and w1 in wordDict:
                    rr = bt(word[j:])
                    for r in rr:
                        res.append(f'{w1} {r}')
                        # res += [f'{w1} {r}' for r in rr]
                    
            return res
 
        return bt(s)

            def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        
        wordDict = set(wordDict)
        
        def bt(i, path):
            if i == len(s):
                res.append(path)
                return
        
            
            for j in range(i + 1, len(s) + 1):
                v = s[i : j]
                # print(v)
                
                if v and v in wordDict:
                    bt(j, f'{path} {v}' if path else f'{v}')
                    
        bt(0, "")
        return res