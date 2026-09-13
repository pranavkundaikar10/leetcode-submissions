class Solution:
    def countSubstrings(self, s: str) -> int:
        total_count = 0

        def expand_center(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count


        for i in range(len(s)):
            total_count += expand_center(i, i)
            total_count += expand_center(i, i+1)

        return total_count
