class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        s = [[nums[0]]]
        # print(len(s[-1]))
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                if len(s[-1]) < 2:
                    s[-1].append(nums[i])
                else:
                    s[-1][-1] = nums[i]
            else:
                s.append([nums[i]])
        
        return [f'{it[0]}->{it[1]}' if len(it) == 2 else f'{it[0]}' for it in s]