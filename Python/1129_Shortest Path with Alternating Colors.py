class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        g = {i: [[],[]] for i in range(n)}
        for i, j in red_edges:
            g[i][0].append(j)
        for i, j in blue_edges:
            g[i][1].append(j)
            
        q = collections.deque([(0, 'r', 0), (0, 'b',0)])
        
        res = [float('inf') for _ in range(n)]
        visited = set()
        while q:
            n, c, l = q.popleft()
            # print(res[l],l)
            res[n] = min(res[n], l)
            if (n, c) not in visited:
                visited.add((n,c))
                if c == 'r':
                    for b in g[n][1]:
                        q.append((b,'b',l + 1))
                else:
                    for r in g[n][0]:
                        q.append((r, 'r', l + 1))
                        
        return [v if v != float('inf') else -1 for v in res]
            