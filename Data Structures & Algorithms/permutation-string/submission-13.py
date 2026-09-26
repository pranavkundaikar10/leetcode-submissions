class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        countS1, countS2 = [0] * 26, [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            countS1[ord(s1[i])-ord('a')] += 1
            countS2[ord(s2[i])-ord('a')] += 1
        
        matches = 0

        for i in range(len(countS1)):
            if countS1[i] == countS2[i]:
                matches += 1

        if matches == 26:
            return True
    
        for i in range(len(s1), len(s2)):
            lChr = ord(s2[i - len(s1)]) - ord('a')
            rChr = ord(s2[i]) - ord('a')

            if countS1[rChr] == countS2[rChr]:
                matches -= 1
            
            countS2[rChr] += 1

            if countS1[rChr] == countS2[rChr]:
                matches += 1


            if countS1[lChr] == countS2[lChr]:
                matches -= 1
            
            countS2[lChr] -= 1

            if countS1[lChr] == countS2[lChr]:
                matches += 1

            if matches == 26:
                return True
            
        return False
