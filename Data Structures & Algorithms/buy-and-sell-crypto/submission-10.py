class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        profit=0
        for r,price in enumerate(prices):
            p=price-prices[l]
            profit=max(profit,p)
            if p<0:
                l=r
        return profit
    