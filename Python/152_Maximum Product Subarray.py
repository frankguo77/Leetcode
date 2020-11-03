class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = p1 = p2 = nums[0]
        for i in range(1, len(nums)):
            p1,p2 = max(nums[i],  nums[i] * p1, nums[i] * p2) , min(nums[i],  nums[i] * p1, nums[i] * p2)
            
            res = max(res, p1, p2)
            # print(res, p1, p2)
            
        return res