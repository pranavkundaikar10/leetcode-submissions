class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cache[i] = max(cache[i-2]+nums[i], cache[i-1])
        print(cache)
        return cache[-1]
