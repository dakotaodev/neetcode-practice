class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l=1
        r=max(piles)
        speed=r

        while l<=r:

            k=(l+r)//2

            t=0
            for p in piles:
                t+=math.ceil(float(p)/k)
            if t<=h:
                # this works woohoo
                speed=k
                # reduce to left half to find lower speed if possible
                r=k-1
            else:
                # this did not work boo
                l=k+1

        return speed            