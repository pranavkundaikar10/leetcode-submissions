class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp, res = defaultdict(int), 0
        for num in nums:
            if mp[num]:
                continue
            ln = 1 + mp[num-1] + mp[num+1]
            res = max(res, ln)
            mp[num] = ln
            mp[num-mp[num-1]] = ln
            mp[num+mp[num+1]] = ln
        return res


        