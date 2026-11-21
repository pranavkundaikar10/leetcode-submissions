class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c, cost = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > cost +1 and grid[nr][nc]!=-1:
                    grid[nr][nc] = cost + 1
                    queue.append((nr, nc, cost + 1))

        


