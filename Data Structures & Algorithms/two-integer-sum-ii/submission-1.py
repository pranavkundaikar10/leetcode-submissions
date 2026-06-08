class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        l, r = 0, len(nums)-1
        while l < r:
            sum = nums[l] + nums[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l+1, r+1]
        