class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maxF = 0
        for num in nums:
            if num == maxF:
                count += 1
            else:
                count -= 1
                if count <= 0:
                    count = 1
                    maxF = num
        return maxF
