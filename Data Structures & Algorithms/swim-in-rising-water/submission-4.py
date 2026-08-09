class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while heap:
            cost, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            if (i, j) == (rows-1, cols-1):
                return cost
            visited.add((i,j))

            for dr, dc in directions:
                nr, nc = i+dr, j+dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
                    heapq.heappush(heap, (max(cost, grid[nr][nc]), nr, nc))
            
        return -1
