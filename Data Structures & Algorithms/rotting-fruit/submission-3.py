class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue and fresh != 0:
            qlen = len(queue)
            for i in range(qlen):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
    
                    if min(nr, nc) >= 0 and nr < rows and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            time += 1
        
        return time if not fresh else -1



                