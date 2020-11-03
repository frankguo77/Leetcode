import functools
class Solution:
    #f(i,j)=min(f(i,j),f(i,k−1)+f(k,j)+max(arr[i:k])∗max(arr[k:j+1]))
    def mctFromLeafValues(self, arr: List[int]) -> int:
        #res = float('inf')
        #@functools.lru_cache
        mem = {}
        def dfs(i, j):
            if i >= j:
                return 0
            
            if (i, j) in mem:
                return mem[(i, j)]
            
            #res = float('inf')
            min_v = min([dfs(i, k - 1) + dfs(k, j) + max(arr[i:k]) * max(arr[k: j + 1]) for k in range(i + 1, j + 1)])
            #print(min_v)
            #res = min_v
            mem[(i, j)] = min_v
            return mem[(i, j)]
        
        return dfs(0, len(arr) - 1)

        def mctFromLeafValues2(self, arr: List[int]) -> int:
            stack = [float('inf')]
            ret = 0
            for c in arr:
                while stack[-1] <= c:
                    tmp = stack.pop()
                    ret += tmp * min(stack[-1], c)
                stack.append(c)
            while len(stack) > 2:
                ret += stack.pop() * stack[-1]
                
            return ret    
                
        
        