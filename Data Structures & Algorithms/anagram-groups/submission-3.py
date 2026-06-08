class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for i in strs:
            freq = [0] * 26
            for j in i:
                freq[ord(j.lower())-ord('a')] += 1
            ana[tuple(freq)].append(i)
        return list(ana.values())

        