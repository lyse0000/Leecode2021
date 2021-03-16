class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        seen, stack, N, M = set(), [(start[0], start[1])], len(maze), len(maze[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while stack:
            x_base, y_base = stack.pop()
            if x_base == destination[0] and y_base == destination[1]:
                return True
            
            for dx, dy in directions:
                x, y = x_base, y_base
                while 0<=x+dx<N and 0<=y+dy<M and maze[x+dx][y+dy]==0:
                    x+=dx
                    y+=dy
                
                # last one must be wall so no need to check 0<=x+dx<N and 0<=y+dy<M for last x, y
                if (x, y) not in seen: 
                    stack.append((x,y))
                    seen.add((x,y))
        return False
