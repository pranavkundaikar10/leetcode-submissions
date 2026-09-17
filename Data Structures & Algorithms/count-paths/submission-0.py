class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        rows, cols = m, n

        def backtrack(r, c):
            if (r >= rows and c < cols) or (r < rows and c >= cols):
                return 0
            if (r == rows-1 and c == cols-1):
                return 1
            
            key = (r, c)
            if key in memo:
                return memo[key]
            
            memo[key] = backtrack(r+1, c) + backtrack(r, c+1)
            return memo[key]


        return backtrack(0, 0)