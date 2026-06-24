class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        total = 0
        for num in nums:
            total += num

        if total % 2 != 0:
            return False

        def dfs(i, currSum):

            if currSum == total / 2:
                return 1

            if currSum > total / 2 or i >= len(nums):
                return 0

            key = (i, currSum)
            if key in memo:
                return memo[key]
            
            select = dfs(i+1, currSum + nums[i])
            skip = dfs(i+1, currSum)
            memo[key] = select or skip
            return memo[key]

        return True if dfs(0, 0) else False