class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j, seen):
            print(i, j)
            if i < 0 or j < 0 or i == rows or j == cols or (i, j) in seen:
                return 0
            seen.add((i, j))
            if grid[i][j] == 0:
                return 0
            # if grid[i][j] == 1:
            area = 1

            area += dfs(i+1, j, seen)
            area += dfs(i-1, j, seen)
            area += dfs(i, j+1, seen)
            area += dfs(i, j-1, seen)
            # seen.remove((i, j))
            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i, j, set())
                    res = max(res, area)
        return res