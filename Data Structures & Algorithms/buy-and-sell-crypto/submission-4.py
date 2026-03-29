class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L=0
        max_profit=0

        for R in range(len(prices)):
            profit=prices[R]-prices[L]
            max_profit=max(profit, max_profit)
            if profit<0:
                L=R

        return max_profit