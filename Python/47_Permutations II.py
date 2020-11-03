class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(candi, path):
            if 0 == len(candi):
                res.append(path[:])
                return
            
            visited = set()
            for i in range(len(candi)):
                if candi[i] in visited:
                    continue
                    
                visited.add(candi[i])
                path.append(candi[i])
                new_candi = candi[:]
                new_candi.pop(i)
                helper(new_candi, path)
                path.pop()
                
        helper(nums, [])
        return res

                res = []
        def helper(candi, path):
            if 0 == len(candi):
                res.append(path[:])
                return
            
            visited = set()
            for i in range(len(candi)):
                if candi[i] in visited:
                    continue
                    
                visited.add(candi[i])
                path.append(candi[i])
                helper(candi[:i] + candi[i + 1:], path)
                path.pop()
                
        helper(nums, [])
        return res