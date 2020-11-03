class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 = None
        n1 = n2 = 0
        for v in nums:
            if v == c1:
                n1 = n1 + 1
            elif v == c2:
                n2 = n2 + 1
            elif n1 == 0:
                c1, n1 = v, 1
            elif n2 == 0:
                c2, n2 = v, 1
            else:
                n1 = n1 - 1
                n2 = n2 - 1
                
        size = len(nums)
        #print(c1, n2)
        
        return [n for n in (c1, c2) 
                   if n is not None and nums.count(n) > size // 3]
        
                
            