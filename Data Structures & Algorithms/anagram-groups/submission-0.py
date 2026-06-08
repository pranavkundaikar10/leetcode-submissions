class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramSets = defaultdict(list)

        for item in strs:
            sortedS = ''.join(sorted(item))
            anagramSets[sortedS].append(item)

        return list(anagramSets.values())



        