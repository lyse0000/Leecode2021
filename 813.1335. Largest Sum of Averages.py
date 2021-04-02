class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        # 花花视频讲得很清楚
        # https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-813-largest-sum-of-averages/
        
        N = len(A)
        
        if N<=K: return sum(A)
        
        dp = [ [0] * N for _ in range(K) ]
        
        # Initialization of 1 st layer
        for i in range(N):
            dp[0][i] = sum(A[0:i+1])/(i+1) 
        
        for ki in range(1, K):
            #dp[k_i][k_i] = dp[k_i-1][k_i-1] + A[k_i]
            for i in range(ki, N):
                for j in range(ki-1, i): # k_i-1 是上一个level的开始
                    value = dp[ki-1][j] + sum(A[j+1:i+1])/(i-j)
                    dp[ki][i] = max(dp[ki][i], value)
            
        return dp[K-1][N-1]

# ========================================================================================================
# 1335. Minimum Difficulty of a Job Schedule
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N, job = len(jobDifficulty), jobDifficulty
        
        dp = [[float('inf')]*N for _ in range(d)]
        
        if d > N: return -1
        if d >= N: return sum(job)
        
        for i in range(N):
            dp[0][i] = max(job[:i+1])
        
        
        for di in range(1, d):
            for i in range(di, N):
                for j in range(di-1, i):
                    value = dp[di-1][j] + max(job[j+1:i+1])
                    dp[di][i] = min(dp[di][i], value)
                    
        return dp[d-1][N-1]
                
                
