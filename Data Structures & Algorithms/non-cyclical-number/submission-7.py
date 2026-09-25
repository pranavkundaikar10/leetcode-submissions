class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            digits = 0
            while num:
                digits += (num % 10) ** 2
                num //= 10
            return digits

        slow, fast = n, get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        print(slow, fast)
        print(fast == 1)
        return fast == 1

        