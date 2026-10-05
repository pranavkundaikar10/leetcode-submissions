class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31
        power = -1 if x < 0 else 1

        x = abs(x)
        res = 0
        while x:
            digit = x % 10
            res = res * 10 + digit
            x = x //10
        return res * power if res <= max_int else 0
            
        