class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        如果是 0 就直接跳过
        """
        A = [1] + [i for i in nums if i>0 ] + [1]
        N = len(A)
        
        dp = [[0]*N for _ in range(N)]
        
        """
        dp [i][j] = 从i -> j 不算i，j ，之内的 i+1,i+2,...,j-2,j-1 的最大爆破value
        
        dp [L][R] = MAX{
                        L*A[i]*R + dp[L][i]+dp[i][R]
                        ...
                        ...
                        ...
                        for i in range(L+1, R) [L+1, R-1]
                    }
        return dp[0][N-1]
        """
        
        for dis in range(2, N):  #  dis = R-L dis = 2 measn: [X, X, X]
                                 #  R = L+dis
            for L in range(0, N-dis): # left + R < N
                R = L+dis
                for i in range(L+1, R):
                    new = A[L]*A[i]*A[R] + dp[L][i] + dp[i][R]
                    dp[L][R] = max(dp[L][R], new)
            
        
        return dp[0][N-1]
