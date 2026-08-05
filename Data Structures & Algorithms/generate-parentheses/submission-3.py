class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, op, cl):
            if len(s) == 2*n:
                res.append(s)
            
            if op < n:
                backtrack(s+"(", op+1, cl)
            
            if cl < op:
                backtrack(s+")", op, cl+1)
        backtrack("", 0, 0)
        return res