class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque([])
        fresh = 0
        map = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        time = 0
        print(queue)
        visited = set()
        while queue and fresh > 0:
            time += 1
            for k in range(len(queue)):
                i, j = queue.popleft()
                print(f'{i}, {j}, {time}')
                for r, c in map:
                    if (0 <= i+r < rows) and (0<=j+c<cols) and grid[i+r][j+c] == 1 and (i+r, j+c) not in visited:
                        visited.add((i+r, j+c))
                        queue.append((i+r, j+c))
                        fresh -=1

        return time if fresh == 0 else -1



        
