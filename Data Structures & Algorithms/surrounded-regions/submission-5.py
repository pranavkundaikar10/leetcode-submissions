class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        
        def backtrack(r, c):
            if min(r, c) < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = "T"
            backtrack(r-1, c)
            backtrack(r+1, c)
            backtrack(r, c-1)
            backtrack(r, c+1)
        
        for r in range(rows):
            for c in range(cols):
                backtrack(r, 0)
                backtrack(r, cols-1)
                backtrack(0, c)
                backtrack(rows-1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

