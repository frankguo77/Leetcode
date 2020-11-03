class Solution:
    #n^3
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        #print(nums)
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
               
            # print(i,target - nums[i], nums[i])
            
            if target - nums[i] < nums[i] and nums[i] >= 0:
                break
                
            
            for j in range (i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                    
                if target - nums[i] - nums[j] < nums[j] and nums[j] >= 0:
                    break
                
                #print(j)
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    sum4 = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum4 == target:
                        res.append([nums[i] , nums[j] , nums[l] , nums[r]])
                        
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        
                        l += 1
                        r -= 1
                    elif sum4 < target:
                        # while l < r and nums[l] == nums[l + 1]:
                        #     l += 1
                        l += 1
                    else:
                        # while l < r and nums[r] == nums[r - 1]:
                        #     r -= 1                        
                        r -= 1
        return res
    #n^2            
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        #nums.sort()
        
        sum2 = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                sum2[s].append((i, j))
                
        # visted = set()
        for v in sum2:
            # if v in visted:
            #     continue
            # visted.add(v)    
            if target - v in sum2:
                for i1, i2 in sum2[v]:
                    for i3, i4 in sum2[target - v]:
                        if (i1 == i2 or i1 == i3 or i1 == i4 or
                            i2 == i3 or i2 == i4 or i3 == i4):
                            continue
                        
                        # if len(set([i1, i2, i3, i4])) < 4:
                        #     continue
                        
                        res.add(tuple(sorted([nums[i1], nums[i2], nums[i3], nums[i4]])))
                        
                # del sum2[target - v] 
                # visted.add(target - v)
                            
                
        
        return [list(v) for v in res]        