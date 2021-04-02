class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        len1, len2 = len(word1), len(word2)
        dp = [[0]*(len1+1) for _ in range(len2+1)]
        
        for x in range(len1+1):
            dp[0][x] = x
            
        for y in range(len2+1):
            dp[y][0] = y
            
        
        for y in range(1, len2+1):
            for x in range(1, len1+1):
                
                if word1[x-1] != word2[y-1]:
                    dp[y][x] = 1 + min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1])
                else:
                    dp[y][x] = dp[y-1][x-1]
        return dp[len2][len1]
