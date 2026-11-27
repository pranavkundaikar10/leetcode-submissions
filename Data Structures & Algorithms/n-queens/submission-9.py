class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        c_set, pos_set, neg_set = set(), set(), set()

        def backtrack(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(0, n):
                if c in c_set or (r+c)in pos_set or (r-c) in neg_set:
                    continue
                
                board[r][c] = "Q"
                c_set.add(c)
                pos_set.add((r+c))
                neg_set.add((r-c))

                backtrack(r+1)

                c_set.remove(c)
                pos_set.remove((r+c))
                neg_set.remove((r-c))
                board[r][c] = "."                

        backtrack(0)
        return res
