class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh=0
        rotten=[]
        ROWS=len(grid)
        COLS=len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    rotten.append((r,c))

        q=deque(rotten)
        minute=0
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        while q and fresh:
            for _ in range(len(q)):

                r,c = q.popleft()

                for dr,dc in directions:
                    nr,nc=r+dr,c+dc

                    if (
                        0<=nr<ROWS
                        and 0<=nc<COLS
                        and grid[nr][nc]==1
                    ):
                        q.append((nr,nc))
                        grid[nr][nc]=-1
                        fresh-=1
            minute+=1

        return -1 if fresh>0 else  minute                        




                   