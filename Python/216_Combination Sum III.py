class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def helper(s, i, path):
            if s == n and len(path) == k:
                res.append(path[:])
                return
            
            if i == 10 or len(path) > k:
                return
            
            path.append(i)
            helper(s + i, i + 1, path)
            path.pop()
            helper(s, i + 1, path)
            
        helper(0, 1, [])
        return res
            