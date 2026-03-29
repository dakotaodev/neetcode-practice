class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area=0
        ROWS=len(grid)
        COLS=len(grid[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(r,c,curr):
            grid[r][c]=0
            curr+=1

            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if (
                    0<=nr<ROWS
                    and 0<=nc<COLS
                    and grid[nr][nc]==1
                ):
                    curr=dfs(nr,nc,curr)

            return curr

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    curr=dfs(r,c,0)
                    area=max(area,curr)
        return area