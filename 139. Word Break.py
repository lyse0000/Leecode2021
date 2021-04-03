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


# ================================================================================================================
# 140. Word Break II
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n, words = len(s), set(wordDict)
        
        if not self.isValid(s, n, words):  return []
        
        dp = [[""]]+[[] for _ in range(n)]
        
        for i in range(n+1):    # 1, 2 ,3
            for j in range(i):  # 0, 1, 2
                if s[j:i] in words:
                    for w in dp[j]:
                        dp[i].append(w+("" if w == "" else " ")+s[j:i])
        return dp[n]
        
    def isValid(self, s, n, words):
        dp = [False]*(n+1)
        dp[0] = True
        
        for i in range(n+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]
