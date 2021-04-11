# 240. Search a 2D Matrix II
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        
        y, x = 0, N-1
        
        while y<M and x>=0:
            if matrix[y][x] == target:
                return True
        
            if matrix[y][x] > target:
                x-=1
            else:
                y+=1
        
        return False



# 74. Search a 2D Matrix I
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        # SLOW
        
        
        M, N = len(matrix), len(matrix[0])
        
        lo, hi = 0, M*N-1
        
        while lo<hi:
            m = (lo+hi)//2
            if matrix[m//N][m%N]==target:
                return True
            if matrix[m//N][m%N]<target:
                lo = m+1
            else:
                hi = m-1
        
        return matrix[lo//N][lo%N] == target
        
        """
        
        M, N = len(matrix), len(matrix[0])
        
        y, x = 0, N-1
        
        while x>=0 and y<M:
            if matrix[y][x] == target:
                return True
            if matrix[y][x] < target:
                y+=1
            else:
                x-=1
        return False
