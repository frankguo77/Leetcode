class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        l = 1
        cnt = 1
        for i in range(1, len(nums)):
            if nums[l - 1] == nums[i]:
                cnt += 1
                if cnt <= 2:
                    nums[l] = nums[i]
                    l += 1
            else:
                nums[l] = nums[i]
                l += 1
                cnt = 1

        return l 

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 2: return len(nums)
        l = 0
        for c in nums:
            if l < 2 or c > nums[l - 2]:
                nums[l] = c
                l += 1


        return l 