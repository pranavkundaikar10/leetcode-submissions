class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                break
            seen.add(n)
            sum = 0
            while n:
                print("n in inner loop", n)
                print(n%10)
                sum += (n % 10)**2
                n = n//10
            n = sum
            print("new n", n)
        return n == 1