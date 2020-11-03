class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        m = {'2':['a','b','c'],
             '3':['d','e','f'],
             '4':['g','h','i'],
             '5':['j','k','l'],
             '6':['m','n','o'],
             '7':['p','q','r', 's'],
             '8':['t','u','v'],
             '9':['w','x','y','z']}
        
        def bt(i, path):
            if i == len(digits):
                res.append(''.join(path))
                return
            
            for c in m[digits[i]]:
                path.append(c)
                bt(i + 1, path)
                path.pop()
                
        bt(0, [])
        return res
                
            
            
            


                
            
        