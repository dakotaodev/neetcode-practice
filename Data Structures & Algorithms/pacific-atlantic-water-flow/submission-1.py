class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac=set()
        atl=set()

        ROWS,COLS=len(heights),len(heights[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c, visited, prevHeight):
            if (
                0<=r<ROWS
                and 0<=c<COLS
                and (r,c) not in visited
                and prevHeight<=heights[r][c]
            ):
                visited.add((r,c))
                dfs(r+1,c,visited,heights[r][c])
                dfs(r-1,c,visited,heights[r][c])
                dfs(r,c+1,visited,heights[r][c])
                dfs(r,c-1,visited,heights[r][c])

        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        
        res=[]

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
