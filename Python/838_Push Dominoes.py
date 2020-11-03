class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = []
        d = "L" + dominoes + "R"
        
        l = 0
        for r in range(1, len(d)):
            if d[r] == '.':
                continue
            
            mid = r - l - 1
            if l:
                res.append(d[l])
            
            if d[l] == d[r]:
                res.append(d[l] * mid)
            elif d[l] == 'L' and d[r] == 'R':
                res.append("." * mid)
            else:
                res.append('R' * (mid // 2) + '.' * (mid % 2) + 'L' * (mid // 2))
            
            l = r
        
        return ''.join(res)

    def pushDominoes(self, dominoes: str) -> str:
        res = list(dominoes)
        d = [(i, c) for i, c in enumerate(dominoes) if c != '.']
        d = [(-1, 'L')] + d + [(len(dominoes), 'R')]
        # print(d)
        
        for (l, lc), (r, rc) in zip(d, d[1:]):
            if lc == rc:
                for k in range(l + 1, r):
                    res[k] = lc
            elif lc > rc: #RL
                for k in range(l + 1, r):
                    if r - k == k - l:
                        res[k] = '.'
                    elif r - k > k - l:
                        res[k] = lc
                    else:
                        res[k] = rc

        
        return ''.join(res)