class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        maxJ, currMax = 0, 0
        for i in range(len(nums)-1):
            maxJ = max(maxJ, i + nums[i])
            if i == currMax:
                jumps += 1
                currMax = maxJ
                if currMax >= len(nums)-1:
                    break
        return jumps