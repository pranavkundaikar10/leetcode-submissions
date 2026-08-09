class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        cols, posDiag, negDiag = set(), set(), set()
        res = []
        def backtrack(row):
            if row == n:
                copy = ["".join(i) for i in board]
                res.append(copy)
                return
            
            for col in range(n):
                if col in cols or row+col in posDiag or row-col in negDiag:
                    continue
                
                cols.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)
                board[row][col] = 'Q'
                backtrack(row+1)
                cols.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)
                board[row][col] = '.'


        backtrack(0)
        return res