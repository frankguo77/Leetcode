class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def bt(i,path):
            if i == len(s) and len(path) == 4:
                res.append(".".join(path))
                return
            
            if i == len(s) or len(path) == 4:
                return
            
            for j in range(1, 4):
                t = s[i: i + j]
                # t = t.lstrip('0')
                # if not t:
                #     t = '0'
                # ti = int(t)
                if not t:
                    continue
                #print(t if t else "Null")
                if int(t) > 255 or (j > 1 and s[i] == '0'):
                    continue
                    
                path.append(t)
                bt(i + j, path)
                path.pop()
        
        bt(0, [])
        return res
            
            
            
            
            
            
                
            
        
        