class Solution:
    def climbStairs(self, n: int) -> int:
        return self.topdown(n)
    
    def topdown(self, n) -> int:
        cache = {}

        def climb(n):

            if n <=2:
                return n
            if n in cache:
                return cache[n]
            
            cache[n] = climb(n-1) + climb(n-2)
            return cache[n]
        
        return climb(n)