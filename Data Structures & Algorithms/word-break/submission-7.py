class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def backtrack(i):
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]
            
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    if backtrack(j):
                        memo[j] = True
                        return memo[j]
                else:
                    continue
            memo[i] = False
            return memo[i]
                    
                    

                
            


        return backtrack(0)

