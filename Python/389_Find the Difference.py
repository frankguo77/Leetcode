class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1 = sum(ord(c) for c in s)
        sum2 = sum(ord(c) for c in t)
        
        return chr(sum2 - sum1)

    def findTheDifference2(self, s: str, t: str) -> str:
        cont1 = collections.Counter(s)
        cont2 = collections.Counter(t)
        
        return list((cont2 - cont1).keys())[0]