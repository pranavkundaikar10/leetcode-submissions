class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        res = 0
        for num in nums:
            if num in mp:
                continue
            length = 1 + mp.get(num-1, 0) + mp.get(num+1, 0)
            res = max(res, length)
            mp[num] = length
            mp[num-mp.get(num-1, 0)] = length
            mp[num+mp.get(num+1, 0)] = length
        return res
