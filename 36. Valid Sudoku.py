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
