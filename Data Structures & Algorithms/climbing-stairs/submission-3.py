class Solution:
    def climbStairs(self, n: int) -> int:
        ### TOP DOWN ###
        # Base Case:f(1)=1, f(2)=2
        # recursion: f(n)=f(n-1)+f(n-2)
        cache={}
        def dp(n):
            if n<=2:
                return n
            if n in cache:
                return cache[n]
            
            cache[n]=dp(n-1)+dp(n-2)
            return cache[n]
        return dp(n)