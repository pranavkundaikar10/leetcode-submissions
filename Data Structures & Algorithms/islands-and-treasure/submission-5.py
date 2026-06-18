class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        map = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def backtrack(i, j, count, visited):

            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == -1 or grid[i][j] < count or (i, j) in visited:
                return

            grid[i][j] = count
            visited.add((i, j))
            for r, c in map:
                backtrack(i+r, j+c, 1+count, visited)
            visited.remove((i, j))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    backtrack(i, j, 0, set())

        
