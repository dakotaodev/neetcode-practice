class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l=0
        for r in range(1, len(prices)):
            profit=prices[r]-prices[l]
            max_profit=max(max_profit, profit)
            if profit<0:
                l=r
        
        return max_profit
