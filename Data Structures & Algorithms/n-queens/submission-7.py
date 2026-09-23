class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]
        col_set, posdiag_set, negdiag_set = set(), set(), set()

        def backtrack(row):
            if row >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col_set or (row+c) in posdiag_set or (row-c) in negdiag_set:
                    continue
                col_set.add(c)
                posdiag_set.add(row+c)
                negdiag_set.add(row-c)
                board[row][c] = "Q"
                backtrack(row+1)
                col_set.remove(c)
                posdiag_set.remove(row+c)
                negdiag_set.remove(row-c)
                board[row][c] = "."
        backtrack(0)
        return res