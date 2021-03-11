class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        seen = set()
        level, q, M, leny, lenx = 1, [], matrix, len(matrix), len(matrix[0])
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        # initalize
        for y in range(leny):
            for x in range(lenx):
                if M[y][x] == 0:
                    q.append((y, x))
                    seen.add((y, x))
                else:
                    M[y][x] = float('inf')
        
        # instead of travel from '1', we travel from '0'
        # color level by level
        while len(seen)<leny*lenx:
            nextq = []
            for (y, x) in q:
                for (dy, dx) in directions:
                    if (y+dy, x+dx) not in seen and 0<=y+dy<leny and 0<=dx+x<lenx:
                        seen.add((y+dy, x+dx))
                        M[y+dy][x+dx] = level
                        nextq.append((y+dy, x+dx))
            q = nextq  
            level+=1              
            
        return M
