class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x:
            digit = x % 10
            x = x // 10
            if res > (max_int - digit)//10:
                return 0
            res = res * 10 + digit
        return res * sign
