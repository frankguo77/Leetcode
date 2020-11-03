class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        merged = []
        heap = []
        k = 0
        for i, l in enumerate(nums):
            if l:
                k += 1
                heapq.heappush(heap, (l[0], 0 , i))
            
        while heap:
            v, i, l_i = heapq.heappop(heap)
            if i + 1 < len(nums[l_i]):
                heapq.heappush(heap, (nums[l_i][i + 1], i + 1, l_i))
            merged.append((v, l_i))
        
        # print(merged)
        l = r = 0
        res = []
        counter = [1] * k
        while r < len(merged):
            counter[merged[r][1]] -= 1
            if counter[merged[r][1]] == 0:
                k -= 1
            
            r += 1

            while k == 0:
                # print(res, merged[r], merged[l])
                if not res or (merged[r - 1][0] - merged[l][0] < res[1] - res[0]) or \
                   (merged[r - 1][0] - merged[l][0] == res[1] - res[0] and merged[l][0] < res[0]):
                    res = [merged[l][0], merged[r - 1][0]]
                counter[merged[l][1]] += 1
                if counter[merged[l][1]] == 1:
                    k += 1
                l += 1
                
            
                
        return res

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        merged = []
        heap = []
        k = 0
        for i, l in enumerate(nums):
            if l:
                k += 1
                heapq.heappush(heap, (l[0], 0 , i))
            
        l = 0
        res = []
        counter = [1] * k
        while heap:
            v, i, l_i = heapq.heappop(heap)
            if i + 1 < len(nums[l_i]):
                heapq.heappush(heap, (nums[l_i][i + 1], i + 1, l_i))
            merged.append((v, l_i))
            counter[l_i] -= 1
            if counter[l_i] == 0:
                k -= 1
                
            while k == 0:          
                # print(res, merged[r], merged[l])
                if not res or (v - merged[l][0] < res[1] - res[0]) or \
                   (v - merged[l][0] == res[1] - res[0] and merged[l][0] < res[0]):
                    res = [merged[l][0], v]
                counter[merged[l][1]] += 1
                if counter[merged[l][1]] == 1:
                    k += 1
                l += 1                
        
                
        return res    

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        merged = []
        heap = []
        k = len(nums)
        for i, l in enumerate(nums):
            for c in l:
                merged.append((c, i))
            
        merged.sort()
        
        # print(merged)
        l = r = 0
        res = []
        counter = [1] * k
        while r < len(merged):
            counter[merged[r][1]] -= 1
            if counter[merged[r][1]] == 0:
                k -= 1
            
            r += 1

            while k == 0:
                # print(res, merged[r], merged[l])
                if not res or (merged[r - 1][0] - merged[l][0] < res[1] - res[0]) or \
                   (merged[r - 1][0] - merged[l][0] == res[1] - res[0] and merged[l][0] < res[0]):
                    res = [merged[l][0], merged[r - 1][0]]
                counter[merged[l][1]] += 1
                if counter[merged[l][1]] == 1:
                    k += 1
                l += 1
                
            
                
        return res            