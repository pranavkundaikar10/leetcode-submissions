class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for item in strs:
            counter = [0] * 26
            for val in item:
                counter[ord(val.lower()) - ord('a')] += 1
            res[tuple(counter)].append(item)
        return list(res.values())
        