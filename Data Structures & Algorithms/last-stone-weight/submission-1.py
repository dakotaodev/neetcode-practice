class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            y=heapq.heappop(stones)
            x=heapq.heappop(stones)

            if x!=y:
                res=(y-x)
                heapq.heappush(stones, res)
            
        return 0 if not stones else stones[0]*-1