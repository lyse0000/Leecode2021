class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        
        dp = [[False]*n for i in range(n)]
        
        count = n
        
        for i in range(n-1,-1,-1):
            dp[i][i] = True
            for dist in range(1, n):
                if i + dist < n:
                    j = i + dist
                    if i + 1 == j:
                        dp[i][j] = s[i] == s[j]
                    else:
                        dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                    
                    if dp[i][j]:
                        count += 1
        return count
