class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def backtrack(i, j):

            if min(i, j) < 0 or i >= rows or j >= cols or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            backtrack(i-1, j)
            backtrack(i+1, j)
            backtrack(i, j-1)
            backtrack(i, j+1)

        for i in range(rows):
            backtrack(i, 0)
            backtrack(i, cols-1)
        
        for j in range(cols):
            backtrack(0, j)
            backtrack(rows-1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
