class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = '()'
        perms = ['']
        for i in range(n):
            newPerms = set()
            for perm in perms:
                for j in range(len(perm)+1):
                    pCopy = str(perm)
                    s = ''
                    if j > 0:
                        s += perm[:j]
                    s += l
                    if j < len(perm) + 1:
                        s += perm[j:]
                    newPerms.add(s)
            perms = newPerms
        return list(perms)


                    

        