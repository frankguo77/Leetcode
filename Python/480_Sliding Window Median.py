import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        a = nums[:k]
        a.sort()
        res =[(a[k // 2] + a[(k - 1) // 2]) / 2]
        for i in range(k, len(nums)):
            a.pop(bisect.bisect_left(a, nums[i - k]))
            bisect.insort_left(a,nums[i])
            res.append((a[k // 2] + a[(k - 1) // 2]) / 2)
        return res
            
        
        