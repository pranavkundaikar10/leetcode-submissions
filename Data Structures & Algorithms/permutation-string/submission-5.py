class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1, countS2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            countS1[ord(s1[i])-ord('a')] += 1
            countS2[ord(s2[i])-ord('a')] += 1
        matches = 0
        for i in range(len(countS1)):
            if countS1[i] == countS2[i]:
                matches += 1

        if matches == 26:
            return True
        j = 0
        for i in range(len(s1), len(s2)):
            val = ord(s2[i]) - ord('a')
            if countS2[val] == countS1[val]:                
                matches -= 1
            countS2[val] += 1

            if countS2[val] == countS1[val]:
                matches += 1

            leftVal = ord(s2[j]) - ord('a')
            if countS2[leftVal] == countS1[leftVal]:                
                matches -= 1
            countS2[leftVal] -= 1
            if countS2[leftVal] == countS1[leftVal]:
                matches += 1
            if matches == 26:
                return True
            j += 1
        return False
