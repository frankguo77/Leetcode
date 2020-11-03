class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = sorted((nums1, nums2), key = len)
        n1, n2 = len(a), len(b)
        if not n1 and not n2:
            return 0
        
        if not n1:
            return (b[(n2 - 1) // 2] + b[n2 // 2]) / 2
        
        
        k = (n1 + n2 + 1) // 2
        l, r = 0, len(a)
        while l < r:
            m1 = l + (r - l) // 2
            m2 = k - m1
            if a[m1] < b[m2 - 1]:
                l = m1 + 1
            else:
                r = m1
                
        m1 = l;
        m2 = k - l;
        
        c1 = max(float('-inf') if m1 <= 0 else a[m1 - 1], 
                 float('-inf') if m2 <= 0 else b[m2 - 1]);
 
        if ((n1 + n2) % 2 == 1):
            return c1;    
        
        c2 = min(float('inf') if m1 >= n1 else a[m1], 
                 float('inf') if m2 >= n2 else b[m2]);
                
        return (c1 + c2) * 0.5;
        
            
        