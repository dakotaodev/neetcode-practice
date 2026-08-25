class Solution:
    def climbStairs(self, n: int) -> int:
        return self.bottomup(n)

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

    def bottomup(self, n) -> int:
        a,b = 1,2
        if n <=2:
            return n
        i=3
        while i <=n: 
            tmp=b
            b=a+b
            a=tmp
            i+=1

        return b










