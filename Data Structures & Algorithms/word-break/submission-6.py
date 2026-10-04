class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = False
        memo = {}
        def backtrack(i):
            # print(f'starting {i=}')
            if i >= len(s):
                # print('succes')
                return True

            if i in memo:
                return memo[i]

            for j in range(i+1, len(s)+1):
                if s[i:j] not in wordDict:
                    # print(f'skipping {s[i:j]=}')
                    continue
                # print(f'found {s[i:j]=}')
                if backtrack(j):
                    memo[i] = True
                    return memo[i]
            memo[i] = False
            return memo[i]

        return backtrack(0)