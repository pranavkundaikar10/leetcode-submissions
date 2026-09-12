class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i])-ord('a')] += 1
            mp[tuple(count)].append(s)

        return list(mp.values())