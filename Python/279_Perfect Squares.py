class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(n**0.5) + 1)]
        #dp[i] min N of i
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for c in squares:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)


        return dp[-1]
        
import collections as c
class Solution:
    def numSquares(self, n: int) -> int:
        q = c.deque([(n, 0)])
        visited = set([n])
        while q:
            num, step = q.popleft()
            if num == 0:
                return step
            
            i = 1
            a = num
            while a >= 0:
                a = num - i*i
                if a not in visited:
                    visited.add(a)
                    q.append((a, step + 1))
                i += 1