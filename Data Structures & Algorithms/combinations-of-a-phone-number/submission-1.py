class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mp = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        res = []

        def backtrack(i, s):
            if len(s) == len(digits):
                res.append(s)
                return

            for j in range(i, len(digits)):
                for k in mp[digits[i]]:
                    backtrack(j+1, s+k)


        backtrack(0, "")
        return res

