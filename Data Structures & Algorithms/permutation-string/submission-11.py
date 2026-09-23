class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cS1, cS2 = [0]*26, [0]*26
        for i in range(len(s1)):
            cS1[ord(s1[i])-ord('a')] += 1
            cS2[ord(s2[i])-ord('a')] += 1

        matches = 0

        for i in range(len(cS1)):
            if cS1[i] == cS2[i]:
                matches += 1

        if matches == 26:
            return True

        for i in range(len(s1), len(s2)):
            rIdx = ord(s2[i])-ord('a')
            lIdx = ord(s2[i - len(s1)])-ord('a')

            if cS1[rIdx] == cS2[rIdx]:
                matches -= 1
            
            cS2[rIdx] += 1
            
            if cS1[rIdx] == cS2[rIdx]:
                matches += 1

            
            if cS1[lIdx] == cS2[lIdx]:
                matches -= 1
            
            cS2[lIdx] -= 1
            
            if cS1[lIdx] == cS2[lIdx]:
                matches += 1
            
            if matches == 26:
                return True

        return False

        