class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        # dp = [[1]*len(matrix[0]) for _ in range(len(matrix))]
        memo = {}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c):
            if min(r, c) < 0 or r >= rows or c >= cols:
                return 0
            key = (r, c)
            if key in memo:
                return memo[key]
            
            side = 0
            for dr, dc in directions:
                nr, nc = dr + r, dc + c                
                if min(nr, nc) < 0 or nr >= rows or nc >= cols or matrix[r][c]>=matrix[nr][nc]:
                    continue
                side = max(side, dfs(nr, nc))

            memo[key] = 1 + side
            return memo[key]

        maxP = 0

        for r in range(rows):
            for c in range(cols):
                maxP = max(maxP, dfs(r, c))
        
        return maxP
        

