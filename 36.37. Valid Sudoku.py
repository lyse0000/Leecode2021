# 36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        """
            0 1 2  3 4 5  6 7 8     
            1                       0   1   2 <= (c//3*3 + r//3)
            2    

            3                      
            4                       3   4   5
            5

            6                      
            7                       6   7   8
            8
        
        """
        
        
        seen = set()
        M, N = len(board), len(board[0])
        
        
        for c in range(M):
            for r in range(N):
                num = board[c][r]
                if "." == num: continue
                    
                row, colum, square = "r"+str(r)+num, "c"+str(c)+num, "sq"+str(c//3*3 + r//3)+num
                if row in seen or colum in seen or square in seen:
                    return False
                seen.add(row)
                seen.add(colum)
                seen.add(square)
                
        return True
    
    
    
# =====================================================================================================    
# 37. Sudoku Solver    
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
                
        """
            0 1 2  3 4 5  6 7 8     
            1                       
            2    
            ...
            6                      
            7                     range = row//3*3 - row//3*3+3
            8
        
        """
        self.board = board
        self.solve()
        
        
    def findEmpty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == ".":
                    return (i, j)
        return (-1, -1)
    
    
    def solve(self):
        c, r = self.findEmpty()
        if c<0: return True
        
        for num in ["1","2","3","4","5","6","7","8","9"]:
            if self.noConflict(c, r, num):
                self.board[c][r] = num
                if self.solve(): return True
                self.board[c][r] = '.'
        
    
    def noConflict(self, col, row, num):
        row_ok = all(self.board[col][r_i] != num for r_i in range(9))
        col_ok = all(self.board[c_i][row] != num for c_i in range(9))
        square_ok = all(self.board[c_i][r_i] != num for r_i in range(row//3*3, row//3*3+3) for c_i in range(col//3*3, col//3*3+3))
        
        return row_ok and col_ok and square_ok
