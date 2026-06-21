class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        def dfs(i, j):
            if min(i, j) < 0 or i >= rows or j >= cols or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                dfs(nr, nc)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count