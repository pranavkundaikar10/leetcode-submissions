class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j, seen):
            if i < 0 or i == rows or j < 0 or j == cols or grid[i][j] == 0 or (i,j) in seen:
                return 0
            count = 1
            seen.add((i, j))
            count += dfs(i+1, j, seen)
            count += dfs(i-1, j, seen)
            count += dfs(i, j-1, seen)
            count += dfs(i, j+1, seen)
            return count

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 1:
                    continue
                count = dfs(i, j, set())
                res = max(res, count)
        return res
        