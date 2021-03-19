class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        N, M, x, y = len(board), len(board[0]), click[0], click[1]
        
        if board[x][y] == 'M': 
            board[x][y] = 'X'
            return board
          
        directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
        
        def dfs(i, j):
            if not 0<=i<N or not 0<=j<M or board[i][j] != 'E': return
            
            Mcount = 0
            for di, dj in directions:
                if 0<=i+di<N and 0<=j+dj<M and board[i+di][j+dj] == 'M':
                    Mcount+=1
                    
            if Mcount>0:
                board[i][j] = str(Mcount)
                return
              
            board[i][j] = 'B'
            
            for di, dj in directions:
                dfs(i+di, j+dj)
        
        dfs(x,y)
        return board
