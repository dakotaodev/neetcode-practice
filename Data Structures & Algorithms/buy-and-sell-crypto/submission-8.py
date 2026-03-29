class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        profit=0
        for i, p in enumerate(prices):
            profit=max(profit, p-prices[l])
            if p-prices[l]<0:
                l=i
            
        return profit