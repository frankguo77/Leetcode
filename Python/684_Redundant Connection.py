class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph  = collections.defaultdict(set)
        
        
        def dfs(s, t):
            if s in seen:
                return False
            
            seen.add(s)
            if s == t:
                return True
            
            return any(dfs(n, t) for n in graph[s])
        
        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)

class DSU:
    def __init__(self):
        self.parent = list(range(1001))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px , py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[px] = py
        return True
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
            

            
                       
  
        