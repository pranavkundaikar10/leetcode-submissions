class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            
            if (i == len(word1) and j < len(word2)):
                return len(word2)-j
            if (j == len(word2) and i < len(word1)):
                return len(word1)-i


            key = (i, j)
            if key in memo:
                return memo[key]

            if word1[i] == word2[j]:
                res = dfs(i+1, j+1)
            else:
                res = min(1+dfs(i+1, j), 1+dfs(i, j+1), 1+dfs(i+1, j+1))
            memo[key] = res
            return memo[key]
        return dfs(0, 0)