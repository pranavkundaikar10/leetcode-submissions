class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):

            if i >= len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            res = False
            for j in range(i, len(s)+1):
                if s[i:j] not in wordDict:
                    continue
                if dfs(j):
                    res = True
                    break
            memo[i] = res
            return memo[i]
        
        return dfs(0)
