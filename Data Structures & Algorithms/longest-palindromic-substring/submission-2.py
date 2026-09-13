class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand_center(l, r):
            nonlocal res
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

        
        for i in range(len(s)):
            expand_center(i, i)
            expand_center(i, i+1)
        return res