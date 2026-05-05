class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results=[]

        for x,y in points:

            d=self.distance(x,y)*-1
            heapq.heappush(results, (d,[x,y]))

            while len(results)>k:
                heapq.heappop(results)

        return [r[1] for r in results]         



    def distance(self, x: int, y: int) -> float:
        return math.sqrt(x**2 + y**2)