class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        fresh = 0
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        print(f'{queue} {fresh}')
        time = 0
        while queue and fresh:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

            time += 1
        print(f'{time}')
        return time if not fresh else -1



