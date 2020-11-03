class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
    #我们只需要不断累加区间个数j-i+1即可（因为[i,j]可以拆分为j-i+1个以A[j]结尾的区间）。        
        def helper(n):
            counter = collections.Counter()
            res = 0
            l = r = 0
            while r < len(A):
                counter[A[r]] += 1
                r += 1
                
                while len(counter) > n:
                    counter[A[l]] -= 1
                    if counter[A[l]] == 0:
                        del counter[A[l]]
                    l += 1
                        
                res += (r - l)
            #print(res)
            return res
        
        return helper(K) - helper(K - 1)
        