class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
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


        for i in range(len(s1), len(s2)):
            leftIdx = ord(s2[i - len(s1)]) - ord('a')
            rightIdx = ord(s2[i]) - ord('a')

            if countS2[rightIdx] == countS1[rightIdx]:
                matches -= 1
            
            countS2[rightIdx] += 1

            if countS2[rightIdx] == countS1[rightIdx]:
                matches += 1

            if countS2[leftIdx] == countS1[leftIdx]:
                matches -= 1

            countS2[leftIdx] -= 1                

            if countS2[leftIdx] == countS1[leftIdx]:
                matches += 1

            if matches == 26: return True
        return False


        