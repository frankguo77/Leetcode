class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for it in intervals:
            if not res or res[-1][1] < it[0]:
                res.append(it)
            elif res and res[-1][1] < it[1]:
                res[-1][1] = it[1]
        
        return res