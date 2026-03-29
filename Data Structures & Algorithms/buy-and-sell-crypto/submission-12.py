class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l=0
        for r,p in enumerate(prices):
            curr=p-prices[l]
            profit=max(profit,curr)
            if curr<0:
                l=r
            
        return profit
