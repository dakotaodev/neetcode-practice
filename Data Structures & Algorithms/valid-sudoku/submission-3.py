class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows=defaultdict(list)
        cols=defaultdict(list)
        squares=defaultdict(list)

        for r in range(9):
            for c in range(9):

                if board[r][c]==".":
                    continue
                val=board[r][c]

                if (
                    val in rows[r]
                    or val in cols[c]
                    or val in squares[(r//3,c//3)]
                ):
                    return False
                
                rows[r].append(val)
                cols[c].append(val)
                squares[(r//3,c//3)].append(val)
        
        return True

