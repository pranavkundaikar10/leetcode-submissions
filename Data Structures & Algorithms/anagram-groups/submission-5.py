class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for j in range(len(s)):
                cnt[ord(s[j])-ord('a')] += 1
            mp[tuple(cnt)].append(s)
        return list(mp.values())

