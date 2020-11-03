    def majorityElement(self, nums: List[int]) -> int:
        candidate = count = 0
        for c in nums:
            if count == 0:
                candidate, count = c, 1
            elif c == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate