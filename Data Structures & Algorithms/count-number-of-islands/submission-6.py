class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)] 
        res=0

        def dfs(r,c):
            grid[r][c]="0"
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if (
                    0<=nr<ROWS
                    and 0<=nc<COLS
                    and grid[nr][nc]=="1"
                ):
                    dfs(nr,nc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    res+=1
                    dfs(r,c)
        return res