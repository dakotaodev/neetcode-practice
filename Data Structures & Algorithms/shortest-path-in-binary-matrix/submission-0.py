class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if not grid or grid[0][0]:
            return -1

        # DIMENSION
        N = len(grid)

        # INIT
        queue=deque()
        queue.append((0,0))
        visited=set()
        visited.add((0,0))
        directions=[(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,1),(1,-1),(-1,-1)]
        length=1

        #BFS
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()

                if (
                    r==N-1
                    and c==N-1
                    and grid[r][c]==0
                ):
                    return length

                for dr, dc in directions:
                    nr,nc=r+dr,c+dc
                    if (
                        min(nr,nc)<0
                        or nr==N
                        or nc==N
                        or (nr,nc) in visited
                        or grid[nr][nc]==1
                    ):
                        continue
                    
                    queue.append((nr,nc))
                    visited.add((nr,nc))

            length+=1
        
        return -1




        