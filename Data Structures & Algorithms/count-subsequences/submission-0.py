class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        memo = {}
        def dfs(i, j):
            if j >= len(t):
                return 1            
            if i >= len(s):
                return 0


            key = (i, j)
            if key in memo:
                return memo[key]
            select = 0
            if s[i] == t[j]:
                select = dfs(i+1, j+1)
            skip = dfs(i+1, j)
            memo[key] = select + skip
            return memo[key]
        return dfs(0, 0)

