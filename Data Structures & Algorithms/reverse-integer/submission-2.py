class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31 - 1
        res = 0
        sign = -1 if x < 0 else 1
        num = abs(x)

        while num:
            digit = num % 10
            num = num // 10
            if res > (max_int - digit) // 10:
                return 0
            res = res * 10 + digit
        
        return res * sign
        