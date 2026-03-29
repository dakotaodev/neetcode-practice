class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None: 

        ROWS=len(grid)
        COLS=len(grid[0])
        land=2147483647
        directions=[(1,0),(0,1),(-1,0),(0,-1)]

        treasure=[]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    treasure.append((r,c))


        q=deque(treasure)
        distance=0

        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                if grid[r][c]==land:
                    grid[r][c]=min(grid[r][c],distance)
                
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if (
                        0<=nr<ROWS
                        and 0<=nc<COLS
                        and grid[nr][nc]==land
                    ):
                        q.append((nr,nc))
            distance+=1
