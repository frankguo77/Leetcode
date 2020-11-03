class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums):
            if (i > 0) and (nums[i - 1] == nums[i]):
                i += 1
                continue
                
            s = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
#                 while l < r and nums[l] == nums[l + 1]:
#                     l += 1
                
#                 while l < r and nums[r] == nums[r - 1]:
#                     r -= 1
                    
                addup = nums[l] + nums[r]
                if addup == s:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1  
                    r -= 1
                elif addup < s:
                    l += 1
                else:
                    r -= 1

            i += 1
        
        return ans
        # return [list(v) for v in ans]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and  nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t == 0:
                    #print(l,r)
                    ans.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                        #print(l,r)

                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
                    #print(r)
                    
                elif t < 0:
                    l += 1
                else:
                    r -= 1
                    
                # print(i, l, r)
        return ans        
                
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            #print(i)
            twosum = -nums[i]
            if twosum < nums[i]:
                break
            
            d = set()
            for j in range (i + 1, len(nums)):
                if twosum - nums[j] in d:
                    t = sorted((nums[i], nums[j], twosum - nums[j]))
                    ans.add(tuple(t))
                d.add(nums[j])

        return [list(t) for t in ans]            
            
            
        