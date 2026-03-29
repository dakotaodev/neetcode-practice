class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count=0
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        ROWS=len(grid)
        COLS=len(grid[0])

        def dfs(row,col):
            grid[row][col]="-1"
            for dr,dc in directions:
                nr,nc=row+dr,col+dc
                if (
                    0<=nr<ROWS
                    and 0<=nc<COLS
                    and grid[nr][nc]=="1"
                ):
                    grid[nr][nc]="0"
                    dfs(nr,nc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    dfs(r,c)
                    count+=1
        return count

