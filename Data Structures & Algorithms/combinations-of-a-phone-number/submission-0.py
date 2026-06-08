class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digMap = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        def backtrack(i, s):
            if len(s) == len(digits):
                if s:
                    res.append(str(s))
                return
            if i == len(digits):
                return
            for val in digMap.get(digits[i]):
                backtrack(i+1, s+val)

        backtrack(0, '')
        return res