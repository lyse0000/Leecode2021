# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _max, lastsmall = 0, prices[0]
        
        for p in prices:
            if p < lastsmall:
                lastsmall = p
            else:
                _max = max(_max, p-lastsmall)

        return _max

# =======================================================================================================
# 122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 7 1 5 3 4 7
        ret = 0
        
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                ret += prices[i]-prices[i-1]
                
        return ret

# =======================================================================================================
# 123. Best Time to Buy and Sell Stock III
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2次dp
        # https://www.youtube.com/watch?v=a8xKiVTpdks&ab_channel=basketwangCoding 篮子王讲得太好了
        N = len(prices)
        dp = [0]*N
        
        _min, val = float('inf'), 0
        for i, p in enumerate(prices):
            _min = min(p, _min)
            val = max(val, p-_min)
            dp[i] = val
        
        _max, val = float('-inf'), 0
        for j in range(N-1,-1,-1):
            _max = max(prices[j], _max)
            val = max(val, _max-prices[j])
            dp[j] +=val
            
        return max(dp)


# =======================================================================================================        
# 309. Best Time to Buy and Sell Stock with Cooldown
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75942/4-line-Python-solution-52-ms
        
        
        3 state: (hold) (empty) (empty_cooldown)
        
        hold --------[sell]--------------> empty_cooldown
        hold --------[do nothing]--------> hold
        empty --------[buy]--------------> hold
        empty --------[do nothing]-------> empty
        empty_cooldown -----[do nothing]-> empty
        
        --------------------------------------------
        hold = -inf  # cannot sell at begining
        empty = 0
        empty_cooldowm = 0
        
        --------------------------------------------
        hold = max of        prev_hold or prev_empty - price
        empty = max of       prev_empty or prev_empty_cooldown
        empty_cooldowm =     prev_hold + price
        
        --------------------------------------------
        
        #               []      6       1       3       8       4       7
        hold           -inf     -6      -1     -1      -1      -1       0
        empty            0      0       0      0        2       7       7
        empty_cooldowm   0      -inf    -5     2       7       -3       6
        
        """
        
        
        hold, empty, empty_cooldown = float('-inf'), 0, 0
        
        for p in prices:
            prev_hold, prev_empty, prev_empty_cooldown = hold, empty, empty_cooldown
            
            hold = max(prev_hold, prev_empty - p)
            empty = max(prev_empty, prev_empty_cooldown)
            empty_cooldown = prev_hold + p
        
        return max(empty, empty_cooldown)
