class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        set_col, set_posdiag, set_negdiag = set(), set(), set()
        res = []

        def backtrack(row):
            if row >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for col in range(len(board[0])):
                if col in set_col or row + col in set_posdiag or row-col in set_negdiag:
                    continue
                
                set_col.add(col)
                set_posdiag.add(row+col)
                set_negdiag.add(row-col)
                board[row][col] = 'Q'
                backtrack(row+1)
                set_col.remove(col)
                set_posdiag.remove(row+col)
                set_negdiag.remove(row-col)
                board[row][col] = '.'

        backtrack(0)
        return res