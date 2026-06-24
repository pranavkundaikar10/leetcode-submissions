class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):

            if i >= len(s):
                return True

            key = i
            if key in memo:
                return memo[key]
            
            ans = False
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    if dfs(j) == True:
                        ans = True
                        break
            memo[key] = ans
            return memo[key]

        return dfs(0)