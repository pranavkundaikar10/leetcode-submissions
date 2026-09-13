class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        n = len(s)
        maxL = 0
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <=2 or dp[i+1][j-1]):
                    l = j - i + 1
                    dp[i][j] = l
                    if l > maxL:
                        start, end, maxL = i, j, l

        return s[start:end+1]

