class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]        
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
        distance = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] != -1 and grid[r][c] > distance:
                    grid[r][c] = distance

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols:
                        continue
                    if grid[nr][nc] != -1 and grid[nr][nc] > distance:
                        queue.append((nr, nc))
            distance += 1





