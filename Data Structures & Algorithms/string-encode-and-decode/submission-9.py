class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for i in strs:
            output += str(len(i)) + '#' + i
        return output

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            count = s[i:j]
            i = j + 1
            j = i + int(count)
            val = s[i:j]
            output.append(val)
            i = j
        return output
