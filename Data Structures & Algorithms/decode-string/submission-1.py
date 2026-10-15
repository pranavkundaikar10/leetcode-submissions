class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        def helper():
            nonlocal i
            res = ""
            count = 0
            tmp = ""

            while i < len(s):
                if s[i].isdigit():
                    count = count * 10 + int(s[i])
                elif s[i] == "[":
                    i += 1
                    res += count * helper()
                    count = 0
                elif s[i] == "]":
                    return res
                else:
                    res += s[i]
                i += 1

            return res
        return helper()
        # number then keep getting the multiple * 10
        # normal character --> directly append to res
        # square open bracket triggers the search space
        # square close bracket appends to res


        

        