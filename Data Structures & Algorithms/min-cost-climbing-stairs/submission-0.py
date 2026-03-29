class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost.append(0)
        # for i in range(len(cost)-3,-1,-1):
        #     cost[i]=cost[i]+min(cost[i+1], cost[i+2])

        # return min(cost[0],cost[1])
        cache=[-1] * len(cost)

        def dp(i):
            if i>=len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = cost[i] + min(dp(i+1),dp(i+2))
            return cache[i]
        
        return min(dp(0), dp(1))


