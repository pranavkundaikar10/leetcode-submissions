class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        map = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])
        res = 0

        for item in grid:
            print(f'{item}')

        def backtrack(i, j, area):
            nonlocal res, map

            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != 1:
                return area

            area += 1
            res = max(res, area)

            grid[i][j] = 0
            for r, c in map:
                area = backtrack(i+r, j+c, area)
            return area

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:
                    area = backtrack(i, j, 0)
                    res = max(res, area)
        return res