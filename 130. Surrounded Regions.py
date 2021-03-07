class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N, M = len(board), len(board[0])
        if N<3 or M<3:
            return
        
        def dfs(x, y, letterPrev, letterNext):
            if 0<=x<N and 0<=y<M and board[x][y] == letterPrev:
                board[x][y] = letterNext
                dfs(x+0, y+1, letterPrev, letterNext)  
                dfs(x+0, y-1, letterPrev, letterNext) 
                dfs(x+1, y+0, letterPrev, letterNext) 
                dfs(x-1, y+0, letterPrev, letterNext)  
                        
        # Change boder O->A    
        for i in range(N):
            dfs(i, 0, "O", "A")
            dfs(i, M-1, "O", "A")
        for j in range(M):
            dfs(0, j, "O", "A")
            dfs(N-1, j, "O", "A")
        
        for i in range(0,N):
            for j in range(0,M):
                # Change all other O->X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # Change all other A->O
                if board[i][j] == "A":
                    board[i][j] = "O"
