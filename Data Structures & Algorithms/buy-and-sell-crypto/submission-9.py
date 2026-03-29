class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        profit=0
        for idx, p in enumerate(prices):
            tmp=p-prices[l]
            profit=max(profit, tmp)
            if tmp<0:
                l=idx
        return profit   