class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        m = collections.defaultdict(dict)
        for (a, b), v in zip(equations, values):
            m[a][b] = v
            m[b][a] = 1.0 / v
        
        
        def dfs(s, e, visited):
            if s == e: 
                return 1.0
            else:
                for n in m[s]:
                    if n not in visited:
                        visited.add(n)
                        d = dfs(n, e,visited)
                        if d > 0.0 : 
                            return m[s][n] * d
                return -1.0
                    
                    
        return [dfs(a, b, set()) if a in m and b in m else -1.0 for a, b in queries]