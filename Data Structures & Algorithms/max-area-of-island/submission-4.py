class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        def dfs(i, j):
            if min(i, j) < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    out = dfs(i, j)
                    res = max(res, out)
        return res


