class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, mp = 0, defaultdict(int)

        for num in nums:
            if mp[num]:
                continue

            sl = mp[num-1] + mp[num+1] + 1
            print(f'{num, mp[num-1], sl}')            
            mp[num] = sl
            res = max(sl, res)
            mp[num-mp[num-1]] = sl
            mp[num+mp[num+1]] = sl
        return res