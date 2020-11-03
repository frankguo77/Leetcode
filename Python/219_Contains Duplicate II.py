class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True
            
            d[v] = i
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i, v in enumerate(nums):
            if v in s:
                return True
            s.add(v)
            
            if len(s) == k + 1:
                s.remove(nums[i - k])
            
            
        return False
                