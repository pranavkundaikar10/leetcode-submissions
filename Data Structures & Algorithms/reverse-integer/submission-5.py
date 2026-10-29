class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31-1
        sign = -1 if x < 0 else 1

        num = abs(x)
        res = 0
        while num:
            if res > (max_int - (num % 10))/10:
                return 0
            res = res * 10 + (num % 10)
            num //= 10
        return sign * res
        