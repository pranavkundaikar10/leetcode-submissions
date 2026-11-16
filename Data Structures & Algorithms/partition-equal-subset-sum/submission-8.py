class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        memo = {}
        def backtrack(i, target):
            if i >= len(nums) or target <= 0:
                if target == 0:
                    return True
                return False
            
            key = (i, target)
            if key in memo:
                return memo[key]
            
            memo[key] = backtrack(i+1, target - nums[i]) or backtrack(i+1, target)
            return memo[key]
        return backtrack(0, target)

