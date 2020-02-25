# import functools

# class Need(dict):
#     def __missing__(self, key):
#         lo, hi = key
#         if lo >= hi:
#             return 0
#         ret = self[lo, hi] = min(x + max(self[lo, x-1], self[x+1, hi])
#                                  for x in range(lo, hi))
#         return ret

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # return Need()[1, n]        
        #@functools.lru_cache
        
        mem = {}
        
        def helper(l, r):  # mincost of [l,  r] 
            if l >= r:
                return 0
            if (l,r) in mem:
                return mem[(l, r)]
            
            res = float('inf')
            for i in range(l, r + 1):
                l_cost = helper(l, i - 1)
                r_cost = helper(i + 1, r)
                res = min(res, i + max(l_cost, r_cost))
            
            mem[(l, r)] = res
            return res
        
        return helper(1, n)
                
                
                
            
            
            
            
            