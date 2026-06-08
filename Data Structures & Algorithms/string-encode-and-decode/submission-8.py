class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output += str(len(i)) + '#' + i
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        print(s)
        while i < len(s):
            count = ''
            while s[i] != '#':
                count += s[i]
                i += 1
            string = ''
            i += 1
            for j in range(int(count)):
                string += s[i]
                i += 1
            output.append(string)
        return output


