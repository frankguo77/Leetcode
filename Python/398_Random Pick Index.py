class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums_start = collections.defaultdict(int)
        
    def pick(self, target: int) -> int:
        start = self.nums_start[target]
        
        try:
            i = self.nums.index(target, start)
        except:
            i = self.nums.index(target, 0)
        self.nums_start[target] = i + 1
        return i
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)