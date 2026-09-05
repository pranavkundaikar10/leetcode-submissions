class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def backtrack(r, c):
            if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            backtrack(r+1, c)
            backtrack(r-1, c)
            backtrack(r, c-1)
            backtrack(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    backtrack(r, c)

        return count
