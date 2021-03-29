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
