class Solution:
    def climbStairs(self, n: int) -> int:
        
        ## top down DP
        # # base cases: n=1=> 1, n=2=>2
        # cache={}

        # def dp(n):
        #     if n<=2:
        #         return n
        #     if n in cache:
        #         return cache[n]
        #     cache[n]=dp(n-1)+dp(n-2)
        #     return cache[n]
        # return dp(n)

        # bottom up DP
        # base cases: n=>1, n-1=>1

        one_before=1
        two_before=1
        for _ in range(n-1):
            current=one_before+two_before
            two_before=one_before
            one_before=current
        
        return one_before
