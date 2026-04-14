class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        max_profit=0
        for i,p in enumerate(prices): 
            profit=p-prices[l]
            max_profit=max(max_profit,profit)
            if profit<0:
                l=i
            
        return max_profit