class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j, distance, visited):
            if i < 0 or j < 0 or i >= rows or j>= cols or grid[i][j] == -1 or grid[i][j] < distance or (i, j) in visited:
                return
            print(f'updating {i}, {j}, {distance}')
            grid[i][j] = distance
            visited.add((i, j))
            dfs(i-1, j, distance + 1, visited)
            dfs(i+1, j, distance + 1, visited)
            dfs(i, j-1, distance + 1, visited)
            dfs(i, j+1, distance + 1, visited)
            visited.remove((i, j))

        for r in range(rows):
            print(f'{grid[r]}')

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    print(f'running {i}, {j}')
                    dfs(i, j, 0, set())