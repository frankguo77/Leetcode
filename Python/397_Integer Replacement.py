class Solution:
    #BFS
    def integerReplacement(self, n: int) -> int:
        q = collections.deque([(n, 0)])
        while q:
            n, level = q.popleft()
            if n == 1:
                return level
            if n & 1 == 0:
                q.append((n >> 1, level + 1))
            else:
                q.append((n - 1 , level + 1))
                q.append((n + 1, level + 1))
        return 0
        
        #DFS
        import functools
        def integerReplacement2(self, n: int) -> int:
            @functools.lru_cache
            def dfs(n):
                if n == 1: return 0
                
                if n & 1 == 0: return 1 + dfs(n >> 1)
                else:
                    return 1 + min(dfs(n - 1), dfs(n + 1))
            
            return dfs(n)

        # Greedy, stolen from orthers.
        def integerReplacement(self, n: int) -> int:
            rst = 0
            while n > 1:
                #even number
                if not n & 1: n >>= 1
                #odd num, last digit is '1', check second last digit
                #end with "..11", add 1, reduce both 1s
                elif n != 3 and (n >> 1) & 1: n += 1
                #end with '..01', deduct 1, make both 0s
                else: n -= 1
                rst += 1
            return rst
            

            
