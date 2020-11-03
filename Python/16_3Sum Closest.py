class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        print(nums)
        
        for i in range(len(nums) - 2):
            #print(len(nums) - 2, i)
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if abs(sum3 - target) < abs(res - target):
                    res = sum3
                    #print(i,l,r, sum3)
                
                if sum3 < target:
                    l += 1
                elif sum3 > target:
                    r -= 1
                else:
                    return sum3
            
        return res
                        


                
            
                
            
        
        