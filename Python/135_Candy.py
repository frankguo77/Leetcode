class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        c = [1] * N
        
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                c[i] = c[i - 1] + 1
                
        # print(c)
                
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and c[i] <= c[i + 1]:
                c[i] = c[i + 1] + 1
        
        # print(c)
        return sum(c)
        