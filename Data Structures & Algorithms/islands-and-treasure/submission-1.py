class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS=len(grid),len(grid[0])
        treasure=[]
        land=2147483647
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    treasure.append([r,c])
        

        q=deque(treasure)
        distances=[(1,0),(0,1),(-1,0),(0,-1)]
        current=1

        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                
                for dr,dc in distances:
                    nr,nc=r+dr,c+dc
                    if (
                        0<=nr<ROWS
                        and 0<=nc<COLS
                        and grid[nr][nc]==land
                    ):
                        grid[nr][nc]=current
                        q.append([nr,nc])
            current+=1
        