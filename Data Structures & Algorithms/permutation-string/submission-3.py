class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countS1, countS2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            countS1[ord(s1[i])-ord('a')] += 1
            countS2[ord(s2[i])-ord('a')] += 1
        
        matches = 0

        for i in range(len(countS2)):
            if countS1[i] == countS2[i]:
                matches += 1
        if matches == 26:
            return True            
        l = 0
        for j in range(len(s1), len(s2)):
            val = ord(s2[j]) - ord('a')

            
            if countS1[val] == countS2[val]:
                matches -= 1
            countS2[val] += 1
            if countS1[val] == countS2[val]:
                matches += 1
            idx = ord(s2[l]) - ord('a')
            if countS1[idx] == countS2[idx]:
                matches -= 1
            countS2[idx] -= 1
            if countS1[idx] == countS2[idx]:
                matches += 1
            l += 1
            if matches == 26:
                return True            
        return False


