class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        #[0:i] no duplicate
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                if i != j:
                    nums[i] = nums[j]
                i += 1
        return i