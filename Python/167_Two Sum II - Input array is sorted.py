class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # if n < 2:
        #     return []
        l, r = 0, n - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return []
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        sums = [0] * (len(nums) + 1)
        res = (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            sums[i] = sums[i - 1] + nums[i - 1] 
        
        def bs(l, r, tar):
            if tar > sums[r]: return -1
            
            while l < r:
                m = l + (r - l) // 2
                if sums[m] < tar:
                    l = m + 1
                else:
                    r = m
            return l
        
        r = len(nums)
        for i in range(len(nums)):
            j = bs(i + 1, r, s + sums[i])
            if j == -1:
                break
            
            # print(j)
            res  = min(res, j - i)
        
        return 0 if res == (len(nums) + 1) else res
                