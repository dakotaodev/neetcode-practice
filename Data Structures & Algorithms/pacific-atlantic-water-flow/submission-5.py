class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pac,atl=set(),set()
        ROWS,COLS=len(heights),len(heights[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c,visited,prev_height):
            visited.add((r,c))

            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if (
                    0<=nr<ROWS
                    and 0<=nc<COLS
                    and (nr,nc) not in visited
                    and heights[nr][nc]>=prev_height
                ):
                    visited.add((nr,nc))
                    dfs(nr,nc,visited,heights[nr][nc])

        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        
        res=[]
        for r,c in pac:
            if (r,c) in atl:
                res.append([r,c])
        return res
