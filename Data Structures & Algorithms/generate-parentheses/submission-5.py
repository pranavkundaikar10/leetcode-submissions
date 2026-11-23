class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(subset, openCount, closeCount):
            if len(subset) == 2 * n:
                res.append(subset)
                return

            if openCount < n:
                backtrack(subset+'(', openCount+1, closeCount)

            if closeCount < openCount:
                backtrack(subset+')', openCount, closeCount + 1)

        backtrack('', 0, 0)
        return res