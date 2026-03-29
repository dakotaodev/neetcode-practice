class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        speed=max(piles)

        while l<=r:
            m=(r+l)//2

            # check if m is viable
            total=0
            for p in piles:
                total+=math.ceil(p/m)
            
            if total<=h:
                speed=min(speed,m)
                r=m-1
            else:
                l=m+1

        return speed        