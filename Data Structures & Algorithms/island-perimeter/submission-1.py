class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 1
            
            if (r, c) in visited:
                return 0

            visited.add((r, c))
            
            total = dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
            # visited.remove((r, c))
            return total



        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
                    break
        
        return res
        