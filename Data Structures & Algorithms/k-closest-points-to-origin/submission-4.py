class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]

        for x,y in points:
            heapq.heappush(res, (-1*self.distance(x,y),[x,y]))
            if len(res)>k:
                heapq.heappop(res) 

        return [r[1] for r in res]

    def distance(self, x:int, y:int) -> float:
        return math.sqrt(x**2+y**2)