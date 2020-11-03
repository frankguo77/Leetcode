class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        l = r = 0
        zeros = 0
        while r < len(A):
            if A[r] == 0:
                zeros += 1
            r += 1
            
            while zeros > K:
                #res = max(res, r - l)
                if A[l] == 0:
                    zeros -= 1
                l += 1
            
            res = max(res, r - l)
        return res
