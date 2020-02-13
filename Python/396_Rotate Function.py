class Solution:
    #TLE
    # def maxRotateFunction(self, A: List[int]) -> int:
    #     n = len(A)
    #     max_v = -float('inf')
    #     for i in range(n):
    #         tmp = 0
    #         for j in range(n):
    #             tmp += j * A[(i + j) % n]
    #         max_v = max(max_v, tmp)
    #     return 0 if max_v == -float('inf') else max_v

    def maxRotateFunction(self, A: List[int]) -> int:
        if not A: return 0
        n = len(A)
        cur, summ = sum(A[i] * i for i in range(n)), sum(A)
        rst = cur
        for k in range(1, n):
            cur = cur + summ - n * A[n-k]
            rst = max(rst, cur)
        return rst  