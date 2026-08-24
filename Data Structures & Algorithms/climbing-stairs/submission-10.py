class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.topdown(n)
        return self.bottomup(n)

    def bottomup(self, n: int) -> int:
        a,b = 1,2
        i = 3
        if n <=2:
            return n
        while i<=n:
            tmp = b
            b= a + b
            a = tmp
            i+=1
        return b

    
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