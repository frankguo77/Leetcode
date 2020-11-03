class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums) + 1) // 2
        nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid::][::-1]

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        
        k = (n + 1) // 2
        
        def findK(s, e, k):
            if s == e:
                return nums[s]
            
            pivot = nums[s]
            i = j = s + 1
            r = e + 1
            #[s + 1, j - 1] < p
            #[j, i - 1] = p
            #[i, r - 1] #unorder
            #[r,] > p
            while i < r:
                if nums[i] == pivot:
                    i += 1
                elif nums[i] > pivot:
                    r = r - 1
                    nums[i], nums[r] = nums[r], nums[i]
                elif nums[i] < pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    j += 1
                    i += 1
                # else:s
                #     i += 1
            nums[s], nums[j - 1] = nums[j - 1], nums[s]
            j = j - 1
            
            if j <= k <= r:
                return nums[j]
            elif j > k:
                return findK(s, j - 1, k)
            elif r < k:
                return findK(r + 1, e, k)
            
        p = findK(0, n - 1, k)
        #p = nums[idx]
        #print(p)
        
        l = 0
        r = n
        i = 0
        while i < r:
            if nums[i] < p:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == p:
                i += 1
            elif nums[i] > p:
                r -= 1
                nums[i], nums[r] = nums[r], nums[i]

                
        #print(nums,k)
        nums[::2], nums[1::2] = nums[:k][::-1], nums[k:][::-1]
            
            
                    
                    
                
            
        

        

            
            
        
        