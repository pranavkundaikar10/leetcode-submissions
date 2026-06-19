class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))

        print(f'{queue}')
        distance = 0
        while queue:
            qLen = len(queue)
            print(f'qLen {qLen}')
            for i in range (qLen):
                r, c = queue.popleft()
                if grid[r][c] != -1 and grid[r][c] > distance:
                    print(f'updating for {i}, {j}, {distance}')
                    grid[r][c] = distance
                
                for dr, dc in directions:
                    if (r+dr) < 0 or (c+dc)< 0 or (r+dr) >= rows or (c+dc) >= cols:
                        continue
                    if grid[r+dr][c+dc] != -1 and grid[r+dr][c+dc] > distance:
                        queue.append((r+dr, c+dc))
            distance += 1

                

