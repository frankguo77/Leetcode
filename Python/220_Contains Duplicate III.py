class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums:
            return False
        
        if k < 1 or t < 0:
            return False
        d = collections.OrderedDict([])
        for c in nums:
            key = c if not t else c // t 
            #print(c ,key)
            for kk in (key - 1, key, key + 1):
                if kk in d and abs(d[kk] - c) <= t:
                    return True
            if key in d:
                del d[key]
            d[key] = c
            if len(d) == k + 1:
                d.popitem(False)
            
        return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums:
            return False
        
        if k < 1 or t < 0:
            return False
        d = {}
        for i, c in enumerate(nums):
            key = c if not t else c // t 
            for kk in (key - 1, key, key + 1):
                if kk in d and abs(d[kk] - c) <= t:
                    return True
            # if key in d:
            #     del d[key]
            d[key] = c
            if len(d) == k + 1:
                del d[nums[i - k] if not t else nums[i - k] // t ]
            
        return False
                