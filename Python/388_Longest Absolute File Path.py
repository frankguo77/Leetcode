class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = [(-1, 0)] #level, len
        res = 0
        for p in input.split('\n'):
            level = p.count('\t')
            p = p.replace('\t', '')
            #print(p, len(p))
            while stack and level <= stack[-1][0]:
                stack.pop()
            if '.' in p:
                res = max(res, stack[-1][1] + len(p))
            else:
                stack.append((level, stack[-1][1] + 1 + len(p)))
                
                
            # if '.' not in p: # table of Contents
            #     stack.append((depth, len(p) + stack[-1][1] + 1))
            # else: # 
            #     max_len = max(max_len, len(p) + stack[-1][1])
        
        return res
        