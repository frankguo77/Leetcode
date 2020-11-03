class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        
        ans = 0
        d_idx = best = 0
        n = len(difficulty)
        worker.sort()
        best = 0
        for w in worker:
            while d_idx < n and w >= jobs[d_idx][0]:
                best = max(best, jobs[d_idx][1])
                d_idx = d_idx + 1
            
            ans += best

        return ans
            