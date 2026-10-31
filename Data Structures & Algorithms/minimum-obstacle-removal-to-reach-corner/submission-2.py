from collections import deque
import heapq
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [(0, 0, 0)]
        visited = set((0, 0))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        cost = 0
        while heap:
            cost, r, c = heapq.heappop(heap)
            if r == rows - 1 and c == cols -1:
                return cost
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if min(nr, nc) < 0 or nr >= rows or nc >= cols or (nr, nc) in visited:
                    continue
                heapq.heappush(heap, ((cost+grid[nr][nc], nr, nc)))
                visited.add((nr, nc))


            
            

            



        
