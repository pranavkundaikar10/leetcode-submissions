class Solution:
    def isHappy(self, n: int) -> bool:
        

        def get_next(n):
            res = 0
            while n:
                digit = n % 10
                n //= 10
                res += digit * digit
            return res
        
        slow, fast = n, get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1
