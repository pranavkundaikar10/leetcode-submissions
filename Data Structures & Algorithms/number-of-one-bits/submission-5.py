class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n:
            n = n & (n-1)
            total += 1
        return total