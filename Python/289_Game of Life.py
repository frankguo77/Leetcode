class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R = len(board)
        if R == 0:
            return 
        C = len(board[0])
        if C == 0:
            return
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        def count1(i, j):
            count = 0
            
            for n in neighbors:
                r, c = i + n[0], j + n[1]
                if r < R and r >= 0 and c < C and c >= 0:
                    count += board[r][c] > 0 
            
            return count

        
       
        for i in range(R):
            for j in range(C):
                s = count1(i, j)
                if board[i][j] == 1 and (s < 2 or s > 3):
                    board[i][j] = 2
                elif board[i][j] == 0 and s == 3:
                    board[i][j] = -1
                    
        for i in range(R):
            for j in range(C):
                if board[i][j] == 2: board[i][j] = 0
                elif board[i][j] == -1:board[i][j] = 1
        
                    
                    
                
                