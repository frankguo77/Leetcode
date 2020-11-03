class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals, newInterval)
        res = []
        for it in intervals:
            if not res or (res[-1][1] < it[0]):
                res.append(it)
            elif res and res[-1][1] < it[1]:
                res[-1][1] = it[1]
        return res
                

        