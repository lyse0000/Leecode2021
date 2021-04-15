class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        很好的解释：https://leetcode.com/problems/frog-jump/discuss/88800/Python-Documented-solution-that-is-easy-to-understand
        
        """
        
        dp = {x: set() for x in stones}
        # edge case
        if stones[1] != 1:
            return False
        
        # jump lenth (k) for reach 1 is always 1
        dp[1].add(1)
        
        for x in stones[1:]:
            for k in dp[x]:
                for ki in range(k-1, k+2):
                    # jump forward
                    if ki > 0 and x+ki in dp:
                        dp[x+ki].add(ki)
        return bool(dp[stones[-1]])
