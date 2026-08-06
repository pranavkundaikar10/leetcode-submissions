class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        time = 0
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while heap:
            time, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r,c))
            if r == len(grid)-1 and c == len(grid[0])-1:
                return time
            
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if min(nr, nc) < 0 or nr >= rows or nc >= cols or (nr, nc) in visited:
                    continue
                heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))

        return time