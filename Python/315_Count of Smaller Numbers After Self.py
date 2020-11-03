class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        sort = []
        for i in reversed(range(0,len(nums))):
            idx = bisect.bisect_left(sort, nums[i])
            sort.insert(idx, nums[i])
            res[i] = idx
            # print(sort, idx)
                    #break
        
        return res