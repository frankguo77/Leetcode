class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums: return 0
        maxReachableDistance = maxNextAvailableDist = steps = 0
        for i in range(len(nums) - 1):
            maxNextAvailableDist = max(maxNextAvailableDist, i + nums[i])
            if i == maxReachableDistance:
                steps += 1
                maxReachableDistance = maxNextAvailableDist
        return steps