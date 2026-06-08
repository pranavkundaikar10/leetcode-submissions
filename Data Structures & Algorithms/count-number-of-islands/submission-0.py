class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, seen):
            if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in seen:
                return
            seen.add((i,j))
            if grid[i][j] == '0':
                return
            grid[i][j] = 0
            for r, c in neighbors:
                dfs(i+r, j+c, seen)

        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i,j, set())
        return islands
        