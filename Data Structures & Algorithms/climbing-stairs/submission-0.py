class Solution:
    def climbStairs(self, n: int) -> int:

        def climb(i):
            if i >= n:
                return n == i
            return climb(i + 1) + climb(i+2)
        
        return climb(0)
