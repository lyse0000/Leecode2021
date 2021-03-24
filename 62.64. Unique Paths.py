# 62. Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]


# =====================================================================================================
# 63. Unique Paths II
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1]*N
        for i in range(N):
            if obstacleGrid[0][i] == 1:
                dp = [1]*(i) +  [0]*(N-i)
                break
        
        for i in range(1, M): 
            dp[0] = (1 - obstacleGrid[i][0]) * dp[0]   #<-- (grid[i][0] and dp[upper level]) != 0
            for j in range(1, N):
                dp[j] = dp[j]+dp[j-1] if obstacleGrid[i][j]==0 else 0
            
        return dp[N-1]


# =====================================================================================================
# 64. Minimum Path Sum
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
            1   3   1 |      [1   4   5]         1  (4)   5        1   4   5        
            1   5   1 |                        [(2) [7]  6]        2   7   6
            4   2   1 |                                            6   8   7  <- ret 7

        """
        M, N, dp = len(grid), len(grid[0]), grid[0][:]
        for i in range(1, N): 
            dp[i] += dp[i-1] 
        
        for i in range(1, M):
            dp[0] += grid[i][0] 
            for j in range(1, N):
                #print(dp)
                dp[j] = min(dp[j], dp[j-1])
                dp[j]+=grid[i][j]
    
        return dp[N-1]
