class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1   
        
        start = 0
        left = 0
        
        for i in range(len(gas)):
            left = left + gas[i] - cost[i]
            if left < 0:
                start = i + 1 
                left = 0
        
        return start