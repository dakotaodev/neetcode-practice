class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        speed=max(piles)

        while l<=r:
            m=(r+l)//2

            # determine if m is a candidate
            total=0
            for p in piles:
                total+=math.ceil(p/m)
            if total<=h:
                # m is viable
                speed=min(speed,m)
                r=m-1
            else:
                #m is not viable
                l=m+1
        return speed        