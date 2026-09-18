class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def backtrack(r, c):
            if r >= m or c >= n:
                return 0
            if r == m-1 and c == n-1:
                return 1
            key = (r, c)
            if key in memo:
                return memo[key]
            
            memo[key] = backtrack(r+1, c) + backtrack(r, c+1)
            return memo[key]
        return backtrack(0, 0)
        