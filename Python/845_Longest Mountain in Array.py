    def longestMountain(self, A: List[int]) -> int:
        #l = 0
        res = 0
        
        #[l: i] mountain
        ups = downs = 0
        for i in range(1, len(A)):
            if ((ups == 0) and A[i - 1] > A[i]):
                 continue
                    
            if A[i - 1] == A[i]:
                ups = downs = 0
                continue
            
            if A[i - 1] < A[i]:
                ups += 1
            else:
                downs += 1
                
            if i == len(A) - 1:
                if ups and downs:
                    res = max(res, ups + downs + 1)
                    
            else:
                if A[i - 1] > A[i] <= A[i + 1]:
                    res = max(res, ups + downs + 1)
                    downs = 0
                    ups = 0
            
            
        return res

    def longestMountain(self, A: List[int]) -> int:
        #l = 0
        res = 0
        
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                l = i - 1
                r = i + 1
                while l > 0 and A[l - 1] < A[l]: l -= 1
                while r < len(A) - 1 and A[r] > A[r + 1]: r += 1
                res = max(r - l + 1, res) 
            
        return res