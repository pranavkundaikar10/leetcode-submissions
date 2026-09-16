class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def backtrack(i):
            if i >= n:
                return 1

            if i in memo:
                return memo[i]
            
            memo[i] = backtrack(i+1) + backtrack(i+2)
            return memo[i]


        return backtrack(1)