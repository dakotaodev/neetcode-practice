class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(list)
        cols=defaultdict(list)
        squares=defaultdict(list)

        for r in range(0,9):
            for c in range(0,9):
                if board[r][c]==".":
                    continue
                v=board[r][c]
                if (
                    v in rows[r]
                    or v in cols[c]
                    or v in squares[(r//3,c//3)]
                ):
                    return False
                
                rows[r].append(v)
                cols[c].append(v)
                squares[((r//3,c//3))].append(v)
        return True