class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        max_ang = ang = 0
        happy_sum = 0
        l = r = 0
        while r < len(customers):
            if grumpy[r] == 0:
                happy_sum += customers[r]
            else:
                ang += customers[r]
            r += 1
                
            
            if r - l == X:
                max_ang = max(ang, max_ang)
                if grumpy[l] == 1:
                    ang -= customers[l]
                l += 1
            
            #max_ang = max(ang, max_ang)
        
        return happy_sum + max_ang
                
     def maxSatisfied2(self, customers: List[int], grumpy: List[int], X: int) -> int:
        max_ang = ang = 0
        happy_sum = 0
        l = r = 0
        while r < len(customers):
            if grumpy[r] == 0:
                happy_sum += customers[r]
            else:
                ang += customers[r]
            r += 1
                
            
            #if r - l == X:
            while r - l > X:
                #max_ang = max(ang, max_ang)
                if grumpy[l] == 1:
                    ang -= customers[l]
                l += 1
            
            max_ang = max(ang, max_ang)
        
        return happy_sum + max_ang       