class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for word in strs:
            cnt = [0] * 26
            for s in word:
                cnt[ord(s)-ord('a')] += 1
            hmap[tuple(cnt)].append(word)
        return list(hmap.values())