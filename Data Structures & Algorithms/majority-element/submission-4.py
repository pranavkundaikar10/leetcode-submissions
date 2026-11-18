class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0
        res = -1
        for num in nums:
            if res == num:
                count += 1
            else:
                count -= 1
                if count < 0:
                    count = 0
                    res = num
        return res


