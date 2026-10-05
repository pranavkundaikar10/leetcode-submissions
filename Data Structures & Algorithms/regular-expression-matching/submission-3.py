class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            key = (i, j)
            if key in memo:
                return memo[key]
            match = (i < len(s) and (s[i]==p[j] or p[j] == "."))

            if j + 1 < len(p) and p[j+1] == "*":
                memo[key] = dfs(i, j+2) or match and dfs(i+1, j)
            else:
                memo[key] = match and dfs(i+1, j+1)
            return memo[key]
        return dfs(0, 0)
