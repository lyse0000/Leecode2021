class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])
        
        dp = [[0]*N for i in range(M)]
        dp[0] = [int(matrix[0][i]) for i in range(N)]
        
        for i in range(1, M):
            dp[i][0] = int(matrix[i][0])
            for j in range(1, N):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1 if matrix[i][j] == "1" else 0
                           
        _max = max(max(row) for row in dp)
        return _max**2
