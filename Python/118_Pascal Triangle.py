class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            row   = [(res[-1][j - 1] if j - 1 >= 0 else 0) +  (res[-1][j] if j < len(res[-1]) else 0)  for j in range(i + 1)]
            
            res.append(row)
            
        return res