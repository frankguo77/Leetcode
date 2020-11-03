class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if not A:
            return 0
        res = 1
        l = 0
        for r in range(1, len(A)):
            if A[r - 1] == A[r]:
                l = r
            else:
                if r == len(A) - 1 or (A[r - 1] <= A[r] <= A[r + 1]) or (A[r - 1] >= A[r] >= A[r + 1]):
                    res = max(r - l + 1, res)
                    l = r
        return res
    #DP
    def maxTurbulenceSize2(self, A: List[int]) -> int:
        if not A:
            return 0
        
        
        res = 1
        curA = curB = 1
        
        for i in range(1, len(A)):
            if A[i - 1] < A[i]:
                curA = curB + 1
                curB = 1
            elif A[i - 1] > A[i]:
                curB = curA + 1
                curA = 1
            else:
                curA = curB = 1
        
            res = max(res, curA, curB)

        return res
                    
        
            