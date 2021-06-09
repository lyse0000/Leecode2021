
class Solution:
    def spiralOrder(self, M: List[List[int]], d = 0) -> List[int]:
        
        nrow, ncol = len(M), len(M[0])
        ret = []
        """
        top_row         
        bottom_row
        
        left_col    right_col    
        """
        top_row, bottom_row = 0, nrow - 1
        left_col, right_col = 0, ncol - 1
        
        while top_row<=bottom_row and left_col<=right_col:
            # right (0, 1)
            if top_row <= bottom_row:
                for j in range(left_col, right_col + 1):
                    ret.append(M[top_row][j])
                top_row += 1
            
            # down (1, 0)
            if left_col <= right_col:
                for i in range(top_row, bottom_row +1):
                    ret.append(M[i][right_col])
                right_col -= 1
                
            # left (0, -1)
            if top_row <= bottom_row:
                for j in range(right_col, left_col-1, -1):
                    ret.append(M[bottom_row][j])
                bottom_row -= 1
            
            # up (-1, 0)
            if left_col <= right_col:
                for i in range(bottom_row, top_row-1, -1):
                    ret.append(M[i][left_col])
                
                left_col += 1
        
        return ret
