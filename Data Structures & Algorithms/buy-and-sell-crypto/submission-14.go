func maxProfit(prices []int) int {

    maxProfit := 0
    curr := 0
    for i,p := range prices {
        profit := p - prices[curr]
        if profit < 0 {
            curr=i
        }
        maxProfit = max(maxProfit, profit)
    }
    
    return maxProfit
}
