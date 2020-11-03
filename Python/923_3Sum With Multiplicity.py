class Solution:
       def threeSumMulti(self, A: List[int], target: int) -> int:
        ct = collections.Counter(A)
        rst = 0
        for i in ct:
            for j in ct:
                if j < i: continue
                k = target - i - j
                if k < j: continue
                if i == j == k: rst += ct[i] * (ct[i] - 1) * (ct[i] - 2) // 6
                elif i == j < k: rst += ct[i] * (ct[i] - 1) // 2 * ct[k]
                elif i < j == k: rst += ct[i] * ct[j] * (ct[j] - 1) // 2
                elif i < j < k: rst += ct[i] * ct[j] * ct[k]
        return rst % (10 ** 9 + 7)
                