class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(list)
        cols=defaultdict(list)
        squares=defaultdict(list)

        for r in range(0,9):
            for c in range(0,9):
                value=board[r][c]
                if value == ".":
                    continue
                
                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in squares[(r//3,c//3)]
                ):
                    return False
                
                rows[r].append(value)
                cols[c].append(value)
                squares[(r//3,c//3)].append(value)
        return True
