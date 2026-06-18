class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols  = len(board), len(board[0])
        def dfs(i, j):

            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)

        for j in range(cols):
            dfs(0, j)
            dfs(rows-1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'
