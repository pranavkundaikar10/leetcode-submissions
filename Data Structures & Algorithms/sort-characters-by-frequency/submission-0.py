class Solution:
    def frequencySort(self, s: str) -> str:
        count = defaultdict(list)
        counts_s = defaultdict(int)

        for i in range(len(s)):
            counts_s[s[i]] += 1

        for key, value in counts_s.items():
            count[value].append(key)
        res = ""
        for i in range(len(s), -1, -1):
            if i in count:
                for num in count[i]:
                    res += i * num

        return res



