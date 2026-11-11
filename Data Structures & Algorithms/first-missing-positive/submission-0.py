class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)

        while i < n:
            val = nums[i]

            if 1 <= val <= n:
                target = val - 1
                if nums[target] != val:
                    nums[i], nums[target] = nums[target], nums[i]
                    continue
            i += 1
        
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return n + 1
        