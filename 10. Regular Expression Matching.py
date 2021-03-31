# https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """     x0 x1
                []  c   c   c   b   c
       y0  {}   T   F   F   F   F   F    
       y1   a   F   F   F   F   F   F
       y2   *   T   F   
            c   F   T
            *   T   
            b   F    
            *   T   
            c   F 
        
        if rule[y] == char or rule[y] == '.':  dp[x][y] = dp[x-1][y-1]
        if rule[y] == '*':
                (1)拿
                    char == rule[y-1]  or rule[y-1] == '.'
                        and 任意一个满足
                        (1.1)        ###AAAAA  *算之前的N个   dp[y][x-1] means同样的rule apply all prev
                        (1.2)            ###A  *只算这一个    dp[y-1][x] means只看前面那个char ma不match
                    
                (2)不拿 -> *当空char
                    dp[y-2][x]    这个留给下一个检验
                
        
        
        """
        lenx, leny, rule, s = len(s)+1, len(p)+1, " "+p, " "+s
        
        dp = [ [False] * lenx for _ in range(leny)]
        dp[0][0] = True
        
        for y in range(1, leny):
            if rule[y] == '*':   dp[y][0] = dp[y-2][0]
            else:   dp[y][0] == False
    
        for y in range(1, leny):
            for x in range(1, lenx):
                if rule[y] == '.' or rule[y] == s[x]:
                    dp[y][x] = dp[y-1][x-1]
                elif rule[y] == '*':
                    dp[y][x] = dp[y-2][x] or ((rule[y-1] == s[x] or rule[y-1] == '.') and (dp[y-1][x] or dp[y][x-1]))
        
        return dp[leny-1][lenx-1]        
