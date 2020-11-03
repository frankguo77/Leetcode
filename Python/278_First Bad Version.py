class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m) == True:
                r = m
            else:
                l = m + 1
        
        if isBadVersion(l) == True:
            return l
        else:
            return -1
        