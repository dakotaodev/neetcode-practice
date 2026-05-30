class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS=len(board),len(board[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1),(0,0)]

        TEMP="T"
        OPEN="O"
        CLOSED="X"
        visited=set()
        def dfs(r,c):
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if (
                    0<=nr<ROWS
                    and 0<=nc<COLS
                    and (nr,nc) not in visited
                    and board[nr][nc]==OPEN
                ):
                    visited.add((nr,nc))
                    board[nr][nc]=TEMP
                    dfs(nr,nc)

        # flip to TEMP
        for r in range(ROWS):
            if board[r][0]==OPEN:
                dfs(r,0)
            if board[r][COLS-1]==OPEN:
                dfs(r,COLS-1)
        for c in range(COLS):
            if board[0][c]==OPEN:
                dfs(0,c)
            if board[ROWS-1][c]==OPEN:
                dfs(ROWS-1,c)

        # capture the others, flip back from TEMP
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]==OPEN:
                    board[r][c]=CLOSED
                elif board[r][c]==TEMP:
                    board[r][c]=OPEN