class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0
        for num in nums:
            if mp[num]:
                continue
            sl = mp[num-1] + mp[num+1] + 1
            res = max(sl, res)
            mp[num] = sl
            mp[num-mp[num-1]] = sl
            mp[num+mp[num+1]] = sl
        return res

        