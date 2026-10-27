class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i]+one, two)
            one = two
            two = curr
        return two