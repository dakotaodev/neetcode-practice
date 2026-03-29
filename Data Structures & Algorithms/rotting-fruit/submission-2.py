class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS,COLS=len(grid),len(grid[0])
        fresh=0
        minutes=0
        rotten=[]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    rotten.append([r,c])

        q=deque(rotten)
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        while fresh and q:
            for _ in range(len(q)):
                r,c=q.popleft()


                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if (
                        0<=nr<ROWS
                        and 0<=nc<COLS
                        and grid[nr][nc]==1
                    ):
                        grid[nr][nc]=2
                        fresh-=1
                        q.append([nr,nc])
            minutes+=1

        return minutes if fresh==0 else -1
