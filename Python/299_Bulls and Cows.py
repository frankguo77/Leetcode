class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        A = B = 0
        for a, b in zip(secret, guess):
            if a == b:
                A += 1
            else:
                d1[a] += 1
                d2[b] += 1
                
        for k in d2:
            if k in d1:
                B += min(d1[k], d2[k])
                
        return f'{A}A{B}B'
        def getHint(self, secret: str, guess: str) -> str:
            from collections import Counter
            s_dic = Counter(secret)
            g_dic = Counter(guess)
            A = sum([s == g for s, g in zip(secret, guess)])
            common = sum((s_dic & g_dic).values())
            B = common - A
            ans = str(A) + 'A' + str(B) + 'B'
            return ans    