class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f'{len(s)}#{s}'
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            wlen = s[i:j]
            word = s[j+1:j+1+int(wlen)]
            res.append(word)
            i = j+1+int(wlen)
            
        return res

        
