class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        """
        Idea is to expend one island by 4 firection. Level by level. 
        Firstly, DFS to find all first island, add to queue
        Secondly, BFS travel level by level
        example:
            1 1 0 0 0
            1 0 0 0 0
            1 0 0 0 2
            0 0 0 0 2
            
            level = 0  ( X = in Seen)
            1 1[X]0 0
            1[X]0 0 0
            1[X]0 0 1
           [X]0 0 0 1
            
            level = 1  ( X = in Seen)
            1 1 X[X]0
            1 X[X]0 0
            1 X[X]0 1
            X[X]0 0 1
            
            level = 2  ( X = in Seen)
            1 1 X X[X]
            1 X X[X]0
            1 X X[X]1
            X X[X]0 1
            
            level = 3  ( X = in Seen)
            1 1 X X X
            1 X X X[X]
            1 X X X [1] <- found another 1 return level = 3
            X X X X 1
        
        """
        
        seen, N, M, q = set(), len(A), len(A[0]), []
        
        def dfs(i,j):
            if (i,j) in seen or not(0<=i<N and 0<=j<M) or A[i][j]==0:
                return
            q.append((i,j))
            seen.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
        
        foundFirst1 = False
        for x in range(N):
            for y in range(M):
                if A[x][y] == 1:
                    foundFirst1 = True
                    dfs(x,y)
                    break
            if foundFirst1:
                break
        
        # now q has all 1 for one island:
        level = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while(True):
            nextq = []
            for (i, j) in q:
                for di,dj in directions:
                    if (i+di, j+dj) not in seen and 0<=i+di<N and 0<=j+dj<M:
                        if A[i+di][j+dj] == 1:
                            return level
                        else:
                            seen.add((i+di, j+dj))
                            nextq.append((i+di, j+dj))
            level+=1
            q = nextq
        return level
        
        
        
        
