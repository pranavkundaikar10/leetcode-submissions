class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        res = []
        rset, pdiag, ndiag = set(), set(), set()
        def backtrack(r):
            if r >= n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in rset or (r+c) in pdiag or (r-c) in ndiag:
                    continue
                rset.add(c)
                pdiag.add((r+c))
                ndiag.add((r-c))
                board[r][c] = 'Q'
                backtrack(r+1)
                rset.remove(c)
                pdiag.remove((r+c))
                ndiag.remove((r-c))
                board[r][c] = '.'        
        backtrack(0)
        return res