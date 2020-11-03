class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.its = []

    def addNum(self, val: int) -> None:
        if not self.its:
            self.its.append([val, val])
            return

        idx = bisect.bisect_left(self.its, [val, val])
        
        if idx < len(self.its) and self.its[idx][0] <= val <= self.its[idx][1]:
            return
        
        if idx > 0 and self.its[idx - 1][0] <= val <= self.its[idx - 1][1]:
            return
        
        addnew = True
        
        if idx > 0 and self.its[idx - 1][1] == val - 1:
            self.its[idx - 1][1] = val
            addnew = False
            
        if idx < len(self.its) and self.its[idx][0] == val + 1:
            self.its[idx][0] = val
            addnew = False
            
        if idx > 0 and idx < len(self.its):
            if self.its[idx - 1][1] == self.its[idx][0]:
                self.its[idx - 1][1] = self.its[idx][1]
                self.its.pop(idx)
        
        if addnew == True:
            self.its.insert(idx, [val, val])
         
        
        

    def getIntervals(self) -> List[List[int]]:
        return self.its
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()