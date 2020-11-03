class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for c in nums:
            if c in s:
                return True
            else:
                s.add(c)
        return False