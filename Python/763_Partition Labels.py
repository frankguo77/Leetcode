from operator import itemgetter 
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        rangeDict = {}
        for i, c in enumerate(S):
            if c not in rangeDict:
                rangeDict[c] = [i, i]
            else:
                rangeDict[c][1] = i
        rangelist = sorted(rangeDict.values(), key = lambda x: (x[0], -x[1]))
        res = []
        cmin = cmax = 0
        for l, r in rangelist:
            if l > cmax:
                res.append(cmax - cmin + 1)
                cmin, cmax = l, r
            else:
                cmax = max(cmax, r)
        res.append(cmax - cmin + 1)
        return res

    def partitionLabels(self, S: str) -> List[int]:
        rangeDict = {}
        for i, c in enumerate(S):
            rangeDict[c] = i
        res = []
        start = end = 0
        for i, c in enumerate(S):
            end = max(end, rangeDict[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
     
        