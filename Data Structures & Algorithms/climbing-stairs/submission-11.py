class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        # if n == 0:
        #     return one

        for i in range(2, n+1):
            tmp = two + one
            one = two            
            two = tmp
        return two

        