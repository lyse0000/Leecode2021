class Solution:
        """
            1   2   3   4   5
        1   1
        2       1
        3         
        4
        
        5   1+4 2+3 3+2 
        6   1+5 2+4 3+3
        
        """       
        dp = [0]*(n+1)
        dp[0:2] = [0,1]

        
        for k in range(2, n+1):
            for i in range(1, k//2+1):
                dp[k] = max(dp[k], dp[i]*dp[k-i])
            if k != n: # not the last one
                dp[k] = max(dp[k], k)
                
        return dp[n]
