# Mydict[(l, r)] max value of (l, r) 
class Mydict(dict):
    def __init__(self, nums):
        self.nums = nums
    def __missing__(self, key):
        l, r = key
        if l >= r - 1:
            return 0
        
        # print(l, r)
        res = max(self.nums[l] * self.nums[i] * self.nums[r] + self[(l, i)] + self[(i, r)] for i in range(l + 1, r))
        self[key] = res
        return res 
        

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        d = Mydict(nums)
        return d[(0, len(nums) - 1)]
        