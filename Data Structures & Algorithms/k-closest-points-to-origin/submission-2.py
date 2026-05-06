class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest=[]

        for x,y in points:

            heapq.heappush(closest, (-1*self.distance(x,y), [x,y]))
            if len(closest)>k:
                heapq.heappop(closest)
            
        return [c[1] for c in closest]

    def distance(self, x: int, y:int) -> float:
        return math.sqrt(x**2 + y**2) 