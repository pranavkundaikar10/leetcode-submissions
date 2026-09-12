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

        if matches == 26: return True

        for rIdx in range(len(s1), len(s2)):
            lIdx = rIdx - len(s1)
            rVal = ord(s2[rIdx])-ord('a')
            if countS1[rVal] == countS2[rVal]:
                matches -= 1
            countS2[rVal] += 1
            if countS1[rVal] == countS2[rVal]:
                matches += 1
            lVal = ord(s2[lIdx])-ord('a')
            if countS1[lVal] == countS2[lVal]:
                matches -= 1
            countS2[lVal] -= 1
            if countS1[lVal] == countS2[lVal]:
                matches += 1
            
            if matches == 26: return True

        return False

        


            
