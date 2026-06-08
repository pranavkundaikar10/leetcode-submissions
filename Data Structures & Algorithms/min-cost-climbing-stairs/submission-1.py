class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        cache[1] = 0
        cache[0] = 0
        for i in range(2, len(cost)+1):
            cache[i] = min(cache[i-1]+cost[i-1], cache[i-2]+cost[i-2])
        print(cache)
        return cache[len(cost)]

