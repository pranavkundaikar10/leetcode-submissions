class Solution:
    def checkValidString(self, s: str) -> bool:
        count_min, count_max = 0, 0

        for c in s:
            if c == '(':
                count_min += 1
                count_max += 1

            if c == ')':
                count_min -= 1
                count_max -= 1

            if c == '*':
                count_min -= 1
                count_max += 1
            
            if count_max < 0:
                return False
            
            if count_min < 0:
                count_min = 0

        return count_min == 0

            