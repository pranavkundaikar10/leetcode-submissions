class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(sub, op, cl):
            if len(sub) == 2 * n:
                res.append(sub)
                return
            
            if op < n:
                dfs(sub+"(", op+1, cl)
            
            if cl < op:
                dfs(sub+")", op, cl+1)

        
        dfs("", 0, 0)
        return res
            