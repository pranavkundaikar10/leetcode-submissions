class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, n = 0, len(digits)-1
        while n >= 0:
            sum = digits[n] + 1
            digits[n] = sum % 10
            carry = sum//10
            if not carry:
                break
            n -= 1
        if carry:
            digits.insert(0, carry)
        return digits
        