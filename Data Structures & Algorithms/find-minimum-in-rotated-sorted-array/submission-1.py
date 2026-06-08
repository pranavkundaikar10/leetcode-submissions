class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            print(nums[l:r+1])
            m = l + (r - l) // 2
            print(m, nums[m])
            if nums[m] < nums[r]:
                r = m
                print(r, nums[r])
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r -= 1
        return nums[l]
        