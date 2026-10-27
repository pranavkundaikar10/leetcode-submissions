class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [0] * cols
        dp[0] = grid[0][0]
        for i in range(1, cols):
            dp[i] = grid[0][i] + dp[i-1]

        for i in range(1, rows):
            for j in range(cols):
                if j > 0:
                    dp[j] = min(dp[j], dp[j-1])
                dp[j] += grid[i][j]
                
        return dp[cols-1]


