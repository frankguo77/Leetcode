class Solution:
    def trap(self, height: List[int]) -> int:
        dpl = [0] * len(height)
        dpr = [0] * len(height)
        res = 0
        
        for i in range(1, len(height)):
            dpl[i] = max(height[i - 1], dpl[i - 1])
            
        for i in range(len(height) - 2, -1, -1):
            dpr[i] = max(height[i + 1], dpr[i + 1])
            
        # print(dpl)
        # print(dpr)
            
        for i in range(len(height)):
            res += max(0, min(dpl[i], dpr[i]) - height[i])
        return res

    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l = 0
        r = len(height) - 1
        maxl = height[0]
        maxr = height[-1]
        res = 0
        
        while l < r:
            if height[l] < height[r]:
                res += max(0, maxl - height[l])
                maxl = max(height[l], maxl)
                l += 1
            else:
                res += max(0, maxr - height[r])
                maxr = max(height[r], maxr)
                r -= 1
            #print(l,r, res)
        
        
        return res
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                h = height[stack.pop()]
                if not stack:
                    break
                res += (min(height[stack[-1]], height[i]) - h)  * (i - stack[-1] - 1) 
                
            stack.append(i)
        return res
        

                
                
                
            
        
        