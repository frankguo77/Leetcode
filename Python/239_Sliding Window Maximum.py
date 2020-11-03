class Solution:
    #brute force
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(0, len(nums) - k + 1): #??len(nums) - k + 1 need to note
            res.append(max(nums[i: i + k]))
        return res

        #max heap
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        res = []
        h = []
        for i in range(len(nums)):
            heapq.heappush(h, -nums[i])
            if i >= k - 1:
                res.append(-h[0])
                h.remove(-nums[i - k + 1])
                heapq.heapify(h)
            
            #res.append(max(nums[i: i + k]))
        return res

    #monotonic queue
    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        
        for i, c in enumerate(nums):
            if q and (i - q[0][0] + 1 > k):
                q.popleft()
            while q and q[-1][1] < c:
                q.pop()
                
            q.append((i, c))
                
            if i >= k - 1:
                res.append(q[0][1])
            
            #res.append(max(nums[i: i + k]))
        return res