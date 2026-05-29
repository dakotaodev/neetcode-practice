class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        LAND=2147483647
        ROWS,COLS=len(grid),len(grid[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        treasure=[]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    treasure.append((r,c))
        
        q=deque(treasure)
        visited=set()
        curr=0
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=curr
                visited.add((r,c))
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if (
                        0<=nr<ROWS
                        and 0<=nc<COLS
                        and (nr,nc) not in visited
                        and grid[nr][nc]==LAND
                    ):
                        visited.add((nr,nc))
                        grid[nr][nc]=curr
                        q.append((nr,nc))
            curr+=1
