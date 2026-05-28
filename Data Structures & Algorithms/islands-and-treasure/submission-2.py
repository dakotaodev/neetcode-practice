class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land=2147483647
        ROWS,COLS=len(grid),len(grid[0])
        treasure=[]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    treasure.append((r,c))
        
        q=deque(treasure)
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        distance=0
        visited=set()
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=distance
                visited.add((r,c))
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if (
                        0<=nr<ROWS
                        and 0<=nc<COLS
                        and (nr,nc) not in visited
                        and grid[nr][nc]==land
                    ):
                        q.append((nr,nc))
                        visited.add((nr,nc))
            distance+=1 