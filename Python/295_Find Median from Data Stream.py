class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.r = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.r, -num)
        v = heapq.heappop(self.r)
        heapq.heappush(self.l, -v)
        
        if len(self.l) - len(self.r) > 1:
            heapq.heappush(self.r, -heapq.heappop(self.l))
        
    def findMedian(self) -> float:
        if not self.l:
            return 0
        if len(self.l) > len(self.r):
            return self.l[0]
        else:
            return (self.l[0] - self.r[0]) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()