class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(start, path):
            res.append(path.copy())
            pre = None
            for i in range(start, len(nums)):
                if pre == nums[i]:
                    continue
                pre = nums[i]
                path.append(nums[i])
                helper(i + 1, path)
                path.pop()
        
        nums.sort()    
        helper(0, [])
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[i])
            helper(i + 1, path)
            path.pop()
            i = i + 1
            while 0 < i < len(nums) and nums[i - 1] == nums[i]:
                i += 1
                
            helper(i, path)
            
            
        nums.sort()
        helper(0, [])
        return res        
            
            
        