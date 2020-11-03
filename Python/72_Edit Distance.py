class Mydict(dict):
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.n1, self.n2 = len(s1), len(s2)
    def __missing__(self, key):
        i, j = key
        if i >= self.n1: 
            return self.n2 - j
        
        if j >= self.n2:
            return self.n1 - i
        
        if self.s1[i] == self.s2[j]:
            res = self[(i + 1, j + 1)]
        else:
            res = min(self[(i, j + 1)], self[(i + 1, j)], self[i + 1, j + 1]) + 1
            
        self[(i,j)] = res
        return res
            
        
import functools            
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #mem = {}
        @functools.lru_cache(maxsize = None)
        def helper(i, j):
            if i >= len(word1):
                return len(word2) - j
            
            if j >= len(word2):
                return len(word1) - i
            
            # if i, j in mem:
            #     return mem[i,j]
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            
            return min(helper(i, j + 1), helper(i + 1, j), helper(i + 1, j + 1)) + 1
        
        return helper(0,0)

    def minDistance(self, word1: str, word2: str) -> int:
        mem = {}
        # @functools.lru_cache(maxsize = None)
        def helper(i, j):
            if i >= len(word1):
                return len(word2) - j
            
            if j >= len(word2):
                return len(word1) - i
            
            if (i, j) in mem:
                return mem[i,j]
            if word1[i] == word2[j]:
                res = helper(i + 1, j + 1)
            else:
                res = min(helper(i, j + 1), helper(i + 1, j), helper(i + 1, j + 1)) + 1
                
            mem[i, j] = res
            return res
        
        return helper(0,0)
            
            
        
        