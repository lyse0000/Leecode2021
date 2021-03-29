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
