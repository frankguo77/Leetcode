class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def solve(m):
            if m > n: 
                return
            
            res.append(m)
            if m * 10 <= n: solve(m * 10)
            
            if m % 10 < 9: solve(m + 1)
        
        solve(1)
        return res

 class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        stack = [1]
        while stack:
            m = stack.pop()
            #print(stack)
            res.append(m)
            if m < n and m % 10 < 9:
                stack.append(m + 1)
            if m * 10 <= n:
                stack.append(m * 10)

        return res       