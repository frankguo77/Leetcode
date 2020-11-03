class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 3:
            return False
        
        v1 = v2 = None
        for c in nums:
            # print(v1, v2, c)
            if v2 != None and c > v2:
                return True
            elif v1 == None or c <= v1:
                v1 = c
            elif v2 == None or c <= v2:
                v2 = c
       
        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 3:
            return False
        
        dp = []
        for c in nums:
            if not dp or c > dp[-1]:
                dp.append(c)
            else:
                idx = bisect.bisect_left(dp, c)
                if dp[idx] > c:
                    dp[idx] = c
            
            if len(dp) == 3:
                return True
            
        return False

                
            