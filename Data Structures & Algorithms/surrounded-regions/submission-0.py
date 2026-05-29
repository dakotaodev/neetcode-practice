class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS=len(board),len(board[0])
        TEMP="T"
        DIRECTIONS=[(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c):
            board[r][c]=TEMP
            for dr,dc in DIRECTIONS:
                nr,nc=r+dr,c+dc
                if (
                    0<=nr<ROWS
                    and 0<=nc<COLS
                    and board[nr][nc]=="O"
                ):
                    dfs(nr,nc)
        
        # from the borders, capture any O's as T
        for r in range(ROWS):
            for c in [0,COLS-1]:
                if board[r][c]=="O":
                    dfs(r,c)
        for c in range(COLS):
            for r in [0,ROWS-1]:
                if board[r][c]=="O":
                    dfs(r,c)
        
        # capture all non temp 
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c]="X"
        # flip temps
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]==TEMP:
                    board[r][c]="O"
