class Solution:
    def solve(self, board: List[List[str]]) -> None:
        grid = board
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] != 'O':
                return
            
            grid[r][c] = 'T'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)


        for r in range(rows):
            if grid[r][0] == 'O':
                dfs(r, 0)
            if grid[r][cols-1] == 'O':
                dfs(r, cols-1)

        for c in range(cols):
            if grid[0][c] == 'O':
                dfs(0, c)

            if grid[rows-1][c] == 'O':
                dfs(rows-1, c)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'
                if grid[r][c] == 'T':
                    grid[r][c] = 'O'

