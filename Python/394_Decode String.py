class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        #result = ""
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                tmp = ''
                #c1 = stack.pop()
                
                while stack[-1] != '[': 
                    c1 = stack.pop()
                    tmp = c1 + tmp
                    
                stack.pop() # pop [
                
                times = ''
                
                while stack and ord("0") <= ord(stack[-1]) <= ord("9"): 
                    t = stack.pop()
                    times = t + times
                
                tmp = int(times) * tmp
                for tmp_c in tmp:
                    stack.append(tmp_c)
                    
        return ''.join(stack)                
                
        