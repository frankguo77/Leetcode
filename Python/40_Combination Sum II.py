class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(s, i, path):
            if s == target:
                res.append(path[:])
                return
            
            if s > target or i == len(candidates):
                return
            
           
            path.append(candidates[i])
            helper(s + candidates[i] , i + 1, path)
            path.pop()
            i = i + 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1
            helper(s, i, path)
            
        candidates.sort()
        helper(0, 0, [])
        return res