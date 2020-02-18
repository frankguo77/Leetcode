class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = list(itertools.accumulate(w))
            

    def pickIndex(self) -> int:
        rand = random.randint(1, self.prefix_sum[-1])
        return bisect.bisect_left(self.prefix_sum, rand)        
        