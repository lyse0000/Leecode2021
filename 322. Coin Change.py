class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        # youtube : https://www.youtube.com/watch?v=ZI17bgz07EE&ab_channel=TECHDOSE
        
        DP table:
        # coins = [2, 1, 4], value = 5
        
        # (1) Intialization
          _________________________________________________________________
                            value
                coin idx |  0       1       2       3       4       5  
                         | --------------------------------------------
     base case->    0    | [0]    [inf]   [inf]   [inf]   [inf]   [inf] 
                    1    | [0]       
                    2    | [0]
                    3    | [0]
          _________________________________________________________________
                
        
        dp[i][j] => min coins that using coins[0 ... i-1] can make to value[j]
        
        dp[i][j] = min( Exclude current coin,  Include one or more current coin)
        
                 = min( 
                        Exclude = dp[i-1][j],
                        Include = 1 + dp[i][j - coins[i-1]] //因为有base case所以-1
                                如果 j-conins[i-1] < i 就是infinity（无解）
                      )


        # (2) Fill the DP
          _______________________________________________________________________________________
                            value
                coin idx |  0           1           2           3           4           5  
                         | ----------------------------------------------------------------------
     base case->    0    |  0           inf         inf         inf         inf         inf  
               (2)  1    |  0       (inf,inf)    (inf,1+0)    (inf,inf)   (inf,1+1)   (inf,inf) 
               (1)  2    |  0       (inf,1)      (1,1+1)      (inf,1+1)   (2,1+2)     (inf,2+1)   
               (4)  3    |  0       (1,inf)      (1,inf)      (2,1+0)     (2,1+1)     (3,1+1) <-ans=2 
          _______________________________________________________________________________________
          从结果可以看出coins不需要排序
          
        """
        
        m, n = len(coins)+1, amount+1
        dp = [[0]*(n) for i in range(m)]
        dp[0] = [0]+[float('inf')]*(n-1)
        
        for i in range(1, m):
            for j in range(1, n):
                exclude = dp[i-1][j]
                include = float('inf') if j-coins[i-1] < 0 else (1 + dp[i][j-coins[i-1]])
                dp[i][j] = min(exclude, include)
        
        return -1 if dp[m-1][n-1] == float('inf') else dp[m-1][n-1]
