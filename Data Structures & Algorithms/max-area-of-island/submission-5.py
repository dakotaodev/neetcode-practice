class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res=0
        ROWS,COLS=len(grid),len(grid[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]


        def bfs(r,c):
            curr=0
            q=deque([(r,c)])
            grid[r][c]=-1
            while q:
                for _ in range(len(q)):
                    r,c=q.popleft()
                    curr+=1
                    for dr,dc in directions:
                        nr,nc=r+dr,c+dc
                        if (
                            0<=nr<ROWS
                            and 0<=nc<COLS
                            and grid[nr][nc]==1
                        ):
                            q.append((nr,nc))
                            grid[nr][nc]=-1
            return curr

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    curr = bfs(r,c)
                    res=max(curr,res)


        return res