class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        color, dic = 2, collections.defaultdict(int)
        
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        
        def dfs(i, j):
            if 0 <= i < M and 0 <= j < N and grid[i][j] == 1: 
                dic[color] += 1
                grid[i][j] = color
                for ii, jj in [(i+1, j),(i-1, j),(i, j+1),(i, j-1)]: 
                    dfs(ii, jj)
        
        ret = 0
        
        # color the map 
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    dfs(i, j)
                    ret = max(ret, dic[color])
                    color+=1
                    
        for i in range(M):
            for j in range(N):
                if grid[i][j]!=0: continue
                    
                temp, seenColor = 1, set()
                for x, y in [(i+1, j),(i-1, j),(i, j+1),(i, j-1)]:
                    if 0<=x<M and 0<=y<N:
                        color = grid[x][y]
                        if not color in seenColor and dic[color]>0:
                            seenColor.add(color)
                            temp+=dic[color]

                ret = max(temp, ret)
            
        return ret
