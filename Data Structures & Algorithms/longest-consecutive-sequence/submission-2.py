class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        map = defaultdict(int)
        for num in nums:
            if map[num]:
                continue
            length = map.get(num-1, 0) + map.get(num+1, 0) + 1
            map[num] = length
            map[num - map[num-1]] = map[num]
            map[num + map[num+1]] = map[num]
            res = max(res, map[num])
        return res