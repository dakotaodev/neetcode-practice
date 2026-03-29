class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        speed=r

        while l<=r:
            m=(l+r)//2

            total=0
            for pile in piles:
                total=total+(math.ceil(float(pile)/m))

            if total<=h:
                speed=min(speed,m)
                r=m-1
            else:
                l=m+1
            
        return speed