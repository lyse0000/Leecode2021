# 139. Word Break
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        N, words = len(s), set(wordDict)
        dp = [False]*(N+1)
        dp[0] = True
        
        for i in range(1, N+1):  # 1,2,3...N+1
            for j in range(i):   # 0,1,2
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[N]
        
