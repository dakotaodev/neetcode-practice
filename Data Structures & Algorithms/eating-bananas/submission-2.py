class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        speed=r
        while l<=r:
            m=(l+r)//2
            # check if m is a viable candidate
            total_time=0
            for p in piles:
                total_time+=math.ceil(float(p)/m)
            if total_time<=h:
                # viable!
                speed=min(speed, m)
                r=m-1
            else:
                # not viable, look in the higher speeds
                l=m+1
        return speed