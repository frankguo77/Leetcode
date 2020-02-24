class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        L = min(rect[0] for rect in rectangles)
        B = min(rect[1] for rect in rectangles)
        R= max(rect[2] for rect in rectangles)
        T = max(rect[3] for rect in rectangles)
        
        points = collections.defaultdict(int)
        for l,b,r,t in rectangles:
            for p, q in zip(((l,b),(r,b),(r,t),(l,t)),(1,2,4,8)):
                if points[p] & q: return False
                points[p] |= q
        
        for p in points:
            if L < p[0] < R or B < p[1] < T:
                if points[p] not in (3, 6, 9, 12, 15):
                    return False
        
        return True

class Solution:
     def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        s = set()
        area = 0
        L = B = float('inf')
        R = T = -float('inf')

        for l,b,r,t in rectangles:
            L = min(L, l)
            B = min(B, b)
            R = max(R, r)
            T = max(T, t)
            for p in ((l,b),(r,b),(r,t),(l,t)):
                if p not in s: 
                    s.add(p)
                else:
                    s.remove(p)
                    
            area += (r - l) * (t - b)
        
        #print(len(s), area, (R - L) * (T - B))
        if len(s) != 4 or \
           (L, B) not in s or \
           (L, T) not in s or \
           (R, B) not in s or \
           (R, T) not in s:
            return False
        
        return area == (R - L) * (T - B)


        
        
        
        
        
        