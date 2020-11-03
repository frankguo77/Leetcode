class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        max_idx = 0 + nums[0]
        for i in range(1, len(nums)):
            if i > max_idx:
                return False
            max_idx = max(max_idx, i + nums[i])
        return True