class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            l, r = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                val = nums[l] + nums[r] + num
                if val < 0:
                    l += 1
                elif val > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        continue
        return res
