class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == res:
                count += 1
            else:
                count -= 1
                if count < 0:
                    res = nums[i]
                    count = 0
        return res



        