class Solution:
    def reverse(self, x: int) -> int:
        power = -1 if x < 0 else 1
        res = 0
        max_int = 2 ** 31 - 1
        x = abs(x)
        while x:
            digit = x%10
            if  res > (max_int - digit)//10:
                return 0
            res = res * 10 + digit
            x = x//10
        return power * res
