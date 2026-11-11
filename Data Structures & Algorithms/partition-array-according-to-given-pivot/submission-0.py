class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = []

        for num in nums:
            if num < pivot:
                res.append(num)

        for num in nums:
            if num == pivot:
                res.append(num)

        for num in nums:
            if num > pivot:
                res.append(num)
        
        return res

