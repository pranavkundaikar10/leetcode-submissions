class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 - obstacleGrid[0][0]


        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                dp[i] = 0
            else:
                dp[i] = dp[i-1]

        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    if j > 0:
                        dp[j] += dp[j-1]

        return dp[n-1]

        

        