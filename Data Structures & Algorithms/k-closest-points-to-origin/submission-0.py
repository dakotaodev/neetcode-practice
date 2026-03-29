import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        heapq.heapify(closest)
        for point in points:
            heapq.heappush(closest, (-1*self.distance(point), point))
            print(closest)
            if len(closest) > k:
                heapq.heappop(closest)

        results = []
        for _ in range(0,k):
            distance, point = heapq.heappop(closest)
            results.append([point[0], point[1]])
        
        return results

    def distance(self, point: List[int]):
        x1 = 0
        y1 = 0
        x2 = point[0]
        y2 = point[1]
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)
        