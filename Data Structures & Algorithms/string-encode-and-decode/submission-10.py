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
            count = int(s[i:j])
            i = j + 1
            j = i + count
            output.append(s[i:j])
            i = j
        return output