class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = ""
        
        for i in range(1, len(strs[0])+1):
            failed = False
            for j in range(1, len(strs)):
                if not strs[j].startswith(strs[0][:i]):
                    failed = True
                    break
            if failed:
                break
            res += strs[0][i-1]
        return res


        