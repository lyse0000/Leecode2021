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
        
