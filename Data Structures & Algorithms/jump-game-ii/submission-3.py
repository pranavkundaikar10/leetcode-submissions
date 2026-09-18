class Solution:
    def jump(self, nums: List[int]) -> int:
        maxJ, currJ, jumps = 0, 0, 0

        for i in range(len(nums)-1):
            maxJ = max(maxJ, i+nums[i])
            if i == currJ:
                jumps += 1
                currJ = maxJ
                if currJ >= len(nums)-1:
                    break
        return jumps
        