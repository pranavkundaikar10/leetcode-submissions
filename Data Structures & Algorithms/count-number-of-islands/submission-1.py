class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        def dfs(i, j, seen):
            if i < 0 or j < 0 or i == rows or j == cols or grid[i][j] in seen or grid[i][j] == '0':
                return
            if grid[i][j] == '1':
                grid[i][j] = '0'
            seen.add((i, j))
            n = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for r, c in n:
                dfs(i+r, c + j, seen)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j, set())
        return count