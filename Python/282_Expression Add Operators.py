class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        if not num:
            return res
        def bt(i, path):
            if i == len(num):
                s = ''.join(path)
                if eval(s) == target:
                    res.append(s)
                
                return
            
            for j in range(i + 1, len(num) + 1):
                v = num[i:j]
                if not v or (j - i > 1 and v[0] == '0'):
                    continue
                    
                path.append(v)
                if j < len(num):
                    for o in ['+', '-', '*']:
                        path.append(o)
                        bt(j, path)
                        path.pop()
                else:
                    bt(j, path)
                    
                path.pop()
                
        bt(0, [])
        return res

    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def bt(i, pre, cur, path):
            # print(pre, cur, path)
            if i == len(num):
                if cur == target:
                    res.append(path)
                return
            
            for j in range(i + 1, len(num) + 1):
                v = num[i:j]
                if not v or (j - i > 1 and v[0] == '0'):
                    break
                    
                v = int(v)
                if not path:
                    bt(j, v, v, f'{v}')
                else:
                    bt(j, v,  cur + v, f'{path}+{v}')
                    bt(j, -v, cur - v, f'{path}-{v}')
                    bt(j, pre * v, cur - pre + pre * v, f'{path}*{v}')
                    
                
        bt(0, 0, 0,"")
        return res
                
            
                
                
        