class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(start, path):
            res.append(list(path))
            for i in range(start, len(nums)):
                path.append(nums[i])
                helper(i + 1, path)
                path.pop()
        helper(0,[])
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, path):
            if i == len(nums):
                res.append(list(path))
                return 

            path.append(nums[i])
            helper(i + 1, path)
            path.pop()
            helper(i + 1, path)
        
        helper(0,[])
        return res                   
                    
                
        