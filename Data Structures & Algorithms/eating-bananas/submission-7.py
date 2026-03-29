class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r=1,max(piles)
        speed=max(piles)

        while l<=r:

            m=(l+r)//2

            # check if m is a viable speed
            hours=0
            for p in piles:
                hours+=math.ceil(p/m)
            if hours<=h:
                # viable candidate
                speed=m
                r=m-1
            else:
                l=m+1        
        return speed

