class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l, r = 0, len(nums)

        while l < r:
            m = (l + r)//2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        res = []
        res.append(l)
        if l == len(nums) or nums[l] != target:
            return [-1,-1]
        l, r = l, len(nums)

        while l < r:
            m = (l + r)//2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        res.append(l-1)
        return res